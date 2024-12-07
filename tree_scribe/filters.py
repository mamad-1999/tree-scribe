# filters.py

# List of directories to exclude
EXCLUDED_DIRECTORIES = [
    '.git',                  # Git version control directory
    '__pycache__',           # Python bytecode cache directory
    '.vscode',               # VS Code workspace settings
    '.idea',                 # JetBrains IDE project settings
    'node_modules',          # Node.js modules directory
    'env',                   # Python virtual environment directory
    'venv',                  # Another common name for Python virtual environments
    'dist',                  # Distribution directory, common in packaging
    'build',                 # Build directory, common in packaging
    '.cache',                # General cache directory
    '.npm',                  # NPM cache directory
    '.gradle',               # Gradle build system cache
    '.tox',                  # Tox testing tool directory
    '.coverage',             # Coverage report directory
    '.pytest_cache',         # Pytest cache directory
    '.mypy_cache',           # Mypy cache directory
    '.ropeproject',          # Rope project directory
    '.svn',                  # Subversion directory
    '.hg',                   # Mercurial directory
    '.next',                 # Next-Js build directory
]
