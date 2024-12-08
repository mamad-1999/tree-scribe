import os
import sys
import argparse
import logging

from tree_scribe.tree import print_directory_tree
from tree_scribe.utils.markdown import export_to_markdown
from tree_scribe.utils.logging_config import setup_logging


def main():
    parser = argparse.ArgumentParser(
        description="Generate and optionally export a directory tree structure.")
    parser.add_argument("directory", help="Path to the root directory")
    parser.add_argument("-md", "--export-md", action="store_true",
                        help="Export the directory structure to a Markdown file")
    parser.add_argument("-d", "--depth", type=int,
                        help="Limit the depth of directory traversal")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose logging")
    parser.add_argument("-c", "--color", action="store_true",
                        help="Enable colorful output")
    parser.add_argument("-s", "--size", action="store_true",
                        help="Show file sizes and line counts")

    args = parser.parse_args()

    if args.verbose:
        setup_logging(level=logging.DEBUG)
    else:
        setup_logging()

    root_dir = args.directory
    export_md = args.export_md
    depth = args.depth
    color = args.color
    show_size = args.size

    if not os.path.isdir(root_dir):
        logging.error(
            "The provided path is not a valid directory. Please try again.")
        sys.exit(1)

    color_mode = color if not export_md else False
    tree_structure, file_count = print_directory_tree(
        root_dir, depth=depth, color_mode=color_mode, show_size=show_size)
    print("\n")
    print(tree_structure)
    print(f"\n├──────── [{file_count} files]")

    if export_md:
        export_to_markdown(root_dir, tree_structure)


if __name__ == "__main__":
    main()
