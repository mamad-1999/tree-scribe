from setuptools import setup, find_packages

setup(
    # Package name (must be unique on PyPI)
    name="tree-scribe",
    version="0.0.4",                     # Initial version
    description="Generate and export directory tree structures with optional color output.",
    author="mamad1999",
    author_email="www.mmhmdmm83@gmail.com",
    url="https://github.com/mamad-1999/tree-scribe",  # Your GitHub URL
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),            # Automatically find all packages
    entry_points={
        "console_scripts": [
            "tree-scribe=tree_scribe.main:main",  # Define the CLI command
        ]
    },
    install_requires=[
        "colorama",                       # Add dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",             # Specify the minimum Python version
)
