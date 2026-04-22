from setuptools import setup, find_packages

setup(
    name="promptmol",
    version="0.1.0",
    description="Natural-language PyMOL assistant — type plain-English prompts, get PyMOL commands",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kody Klupt",
    url="https://github.com/KodyKlupt/PromptMOL",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "anthropic>=0.20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Force Compatible",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
