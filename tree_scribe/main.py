import os
import sys
import argparse
import logging

from tree_scribe.tree import print_directory_tree
from tree_scribe.utils.markdown import export_to_markdown
from tree_scribe.utils.logging_config import setup_logging


def main():
    parser = argparse.ArgumentParser(
        prog="tree-scribe",
        description=(
            "Generate a directory tree structure for a given path, "
            "with options for depth limitation, colorful output, file sizes, "
            "and exporting to Markdown."
        ),
        epilog=(
            "Examples:\n"
            "  tree-scribe /path/to/directory\n"
            "  tree_scribe /path/to/directory -s -c -d 0 --exclude dist build .git"
            "  tree-scribe /path/to/directory -md -c\n\n"
            "For full details, refer to the documentation or use --help."
        ),
        formatter_class=argparse.RawTextHelpFormatter  # Preserve newlines in the epilog
    )

    # Define arguments
    parser.add_argument(
        "directory",
        help="Path to the root directory to analyze"
    )
    parser.add_argument(
        "-md", "--export-md",
        action="store_true",
        help="Export the directory structure to a Markdown file"
    )
    parser.add_argument(
        "-d", "--depth",
        type=int,
        help="Limit the depth of directory traversal (e.g., -d 2)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging for debugging purposes"
    )
    parser.add_argument(
        "-c", "--color",
        action="store_true",
        help="Enable colorful output for better readability"
    )
    parser.add_argument(
        "-s", "--size",
        action="store_true",
        help="Show file sizes and line counts in the output"
    )
    parser.add_argument(
        "--exclude",
        nargs='+',
        help="Exclude specific directories from the output (e.g., --exclude .git .next)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Setup logging based on verbosity
    if args.verbose:
        setup_logging(level=logging.DEBUG)
    else:
        setup_logging()

    # Retrieve and validate root directory
    root_dir = args.directory
    if not os.path.isdir(root_dir):
        logging.error(
            "The provided path is not a valid directory. Please try again."
        )
        sys.exit(1)

    # Extract other arguments
    export_md = args.export_md
    depth = args.depth
    color = args.color
    show_size = args.size
    exclude = args.exclude or []

    # Disable color mode if exporting to Markdown
    color_mode = color if not export_md else False

    # Generate directory tree
    tree_structure, file_count = print_directory_tree(
        root_dir, depth=depth, color_mode=color_mode, show_size=show_size, exclude=exclude
    )

    # Print the tree structure
    print("\n" + tree_structure)
    print(f"\n├──────── [{file_count} files]")

    # Export to Markdown if the flag is enabled
    if export_md:
        export_to_markdown(root_dir, tree_structure)


if __name__ == "__main__":
    main()
