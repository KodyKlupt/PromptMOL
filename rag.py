"""RAG (Retrieval-Augmented Generation) for PyMOL documentation.

Builds a persistent ChromaDB index from the bundled docs/ directory and
retrieves relevant chunks at query time to inject into the system prompt.
Only used when backend is lmstudio (local model).
"""

import os
from typing import List

DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")
CHROMA_DIR = os.path.expanduser("~/.promptmol_rag")
COLLECTION_NAME = "pymol_docs"
MODEL_NAME = "all-MiniLM-L6-v2"

# Module-level singletons — loaded once per session
_embed_model = None
_chroma_client = None
_collection = None


def _get_embed_model():
    global _embed_model
    if _embed_model is None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError:
            raise RuntimeError(
                "sentence-transformers not installed. Run: pip install sentence-transformers"
            )
        _embed_model = SentenceTransformer(MODEL_NAME)
    return _embed_model


def _get_collection(create: bool = False):
    global _chroma_client, _collection
    try:
        import chromadb
    except ImportError:
        raise RuntimeError(
            "chromadb not installed. Run: pip install chromadb"
        )

    if _chroma_client is None:
        _chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)

    if _collection is None or create:
        if create:
            try:
                _chroma_client.delete_collection(COLLECTION_NAME)
            except Exception:
                pass
        _collection = _chroma_client.get_or_create_collection(
            COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


def _load_chunks(docs_dir: str) -> List[dict]:
    """Load all .md/.txt files and split into header-delimited chunks."""
    import re

    chunks = []
    for fname in sorted(os.listdir(docs_dir)):
        if not fname.endswith((".md", ".txt")):
            continue
        path = os.path.join(docs_dir, fname)
        with open(path) as f:
            text = f.read()

        # Split on markdown headers (##, ###) to get topic-level chunks
        parts = re.split(r"\n(?=#{1,3} )", text)
        if len(parts) <= 1:
            # No headers — split on double newlines
            parts = [p for p in text.split("\n\n") if p.strip()]

        for i, part in enumerate(parts):
            part = part.strip()
            if len(part) < 60:
                continue
            chunks.append({
                "id": f"{fname}_{i}",
                "text": part,
                "source": fname,
            })
    return chunks


def build_index(docs_dir: str = DOCS_DIR, force: bool = False) -> int:
    """Build or rebuild the ChromaDB vector index from docs/.

    Returns the number of chunks indexed.
    Skips rebuild if the collection already has the expected chunk count
    (unless force=True).
    """
    chunks = _load_chunks(docs_dir)
    if not chunks:
        raise RuntimeError(f"No .md/.txt files found in {docs_dir}")

    collection = _get_collection(create=False)
    existing = collection.count()

    if not force and existing == len(chunks):
        return existing

    # Rebuild from scratch
    collection = _get_collection(create=True)
    model = _get_embed_model()

    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=False).tolist()

    collection.add(
        ids=[c["id"] for c in chunks],
        documents=texts,
        embeddings=embeddings,
        metadatas=[{"source": c["source"]} for c in chunks],
    )
    return len(chunks)


def is_indexed() -> bool:
    """Return True if the index exists and has content."""
    try:
        col = _get_collection()
        return col.count() > 0
    except Exception:
        return False


def retrieve(query: str, k: int = 3) -> List[str]:
    """Return top-k relevant doc chunks for the given query string."""
    collection = _get_collection()
    if collection.count() == 0:
        return []

    model = _get_embed_model()
    query_embedding = model.encode([query]).tolist()

    n = min(k, collection.count())
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n,
        include=["documents"],
    )
    return results["documents"][0]


def get_context_block(query: str, k: int = 3) -> str:
    """Return a formatted string block to append to the system prompt.

    Returns empty string if RAG is not indexed or retrieval fails.
    """
    try:
        chunks = retrieve(query, k=k)
    except Exception:
        return ""

    if not chunks:
        return ""

    joined = "\n\n---\n\n".join(chunks)
    return (
        "\n\n## Retrieved PyMOL reference (relevant to this request)\n\n"
        + joined
    )


def ensure_index(docs_dir: str = DOCS_DIR) -> bool:
    """Build the index if it doesn't exist yet. Returns True if ready.

    Silent — does not print on success, only on first-time build.
    """
    try:
        if is_indexed():
            return True
        print("PromptMol RAG: building doc index (first run)…")
        n = build_index(docs_dir)
        print(f"PromptMol RAG: indexed {n} chunks. Ready.")
        return True
    except Exception as e:
        print(f"PromptMol RAG: index build failed — {e}")
        return False
