def get_scene_state() -> str:
    """Return a concise summary of the current PyMOL scene for the LLM.

    Includes per-object chain IDs, ligand residue names, and atom counts
    so the LLM can write correct, unambiguous selections without guessing.
    """
    try:
        from pymol import cmd, stored

        objects = cmd.get_object_list() or []
        selections = [
            s for s in (cmd.get_names("selections") or []) if not s.startswith("_")
        ]

        lines = ["Current PyMOL scene:"]

        if not objects:
            lines.append("  No objects loaded.")
            if selections:
                lines.append(f"  Named selections: {', '.join(selections)}")
            return "\n".join(lines)

        for obj in objects:
            try:
                chains = cmd.get_chains(obj) or []
                n_atoms = cmd.count_atoms(obj)

                # Ligand residue names (hetatm, excluding common solvents)
                stored.ligs = []
                cmd.iterate(
                    f"({obj}) and hetatm and not (resn HOH or resn WAT or resn H2O)",
                    "stored.ligs.append(resn)",
                )
                unique_ligs = list(dict.fromkeys(stored.ligs))  # ordered dedup

                parts = []
                if chains:
                    parts.append(f"chains [{', '.join(chains)}]")
                else:
                    parts.append("no chains")
                if unique_ligs:
                    parts.append(f"ligands: {', '.join(unique_ligs)}")
                parts.append(f"{n_atoms} atoms")

                lines.append(f"  {obj}: {', '.join(parts)}")
            except Exception as obj_err:
                lines.append(f"  {obj}: (could not read details: {obj_err})")

        if selections:
            lines.append(f"  Named selections: {', '.join(selections)}")

        return "\n".join(lines)

    except Exception as e:
        return f"(Could not read scene state: {e})"
