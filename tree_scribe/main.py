import os
import sys
import argparse
import logging
from traceback import format_list

from tree_scribe.filters import EXCLUDED_DIRECTORIES

# Import colorama only if the -c switch is used
colorama_enabled = False
if '--color' in sys.argv or '-c' in sys.argv:
    from colorama import Fore, Style, init
    init(autoreset=True)
    colorama_enabled = True

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Global set to track visited directories
visited_directories = set()


def get_colorama_color():
    if colorama_enabled:
        return Fore.GREEN, Fore.CYAN
    else:
        return '', ''


def format_size(size):
    """Format file size in human-readable form."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def calculate_folder_size(folder_path):
    """Calculate the total size of all files in a folder."""
    total_size = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except Exception as e:
                logging.debug(f"Error getting size for {file_path}: {e}")
    return total_size


def print_directory_tree(root_dir, indent="", depth=None, current_depth=0, color_mode=False):
    if depth is not None and current_depth > depth:
        return "", 0

    # Check if the current directory is a symlink
    if os.path.islink(root_dir):
        logging.debug(f"Skipping symlink: {root_dir}")
        return "", 0

    # Avoid infinite loops by checking visited directories
    if root_dir in visited_directories:
        return "", 0

    visited_directories.add(root_dir)

    try:
        items = [item for item in sorted(os.listdir(root_dir))
                 if not (os.path.isdir(os.path.join(root_dir, item)) and item in EXCLUDED_DIRECTORIES)]
    except PermissionError as e:
        logging.error(f"Permission denied: {root_dir}")
        return "", 0
    except Exception as e:
        logging.error(f"Error reading directory {root_dir}: {e}")
        return "", 0

    dir_color, file_color = get_colorama_color() if color_mode else ('', '')
    # Define size and line count color
    size_color = Fore.MAGENTA if color_mode else ''
    reset_color = Style.RESET_ALL if color_mode else ''

    tree_structure = ""
    file_count = 0
    for index, item in enumerate(items):
        path = os.path.join(root_dir, item)
        is_last = index == len(items) - 1
        if os.path.isdir(path):
            # Calculate folder size
            folder_size = calculate_folder_size(path)
            size_str = f"{size_color}({format_size(folder_size)}){reset_color}"
            tree_structure += f"{indent}├── {dir_color}{item}/ {size_str}\n" if color_mode else f"{indent}├── {item}/ {size_str}\n"
            new_indent = indent + "│   " if not is_last else indent + "    "
            subdir_structure, subdir_file_count = print_directory_tree(
                path, new_indent, depth, current_depth + 1, color_mode)
            tree_structure += subdir_structure
            file_count += subdir_file_count
        else:
            # Get file size and line count
            try:
                file_size = os.path.getsize(path)
                file_size_str = format_size(file_size)

                with open(path, "r", encoding="utf-8", errors="ignore") as file:
                    line_count = sum(1 for _ in file)
                line_info = f"{size_color}({line_count} lines, {file_size_str}){reset_color}"
            except Exception as e:
                logging.debug(f"Error reading file {path}: {e}")
                line_info = f"{size_color}(Unreadable){reset_color}"

            tree_structure += f"{indent}├── {file_color}{item} {line_info}\n" if color_mode else f"{indent}├── {item} {line_info}\n"
            file_count += 1
    return tree_structure, file_count


def export_to_markdown(root_dir, tree_structure):
    md_filename = os.path.join(root_dir, "directory_structure.md")
    try:
        with open(md_filename, "w") as md_file:
            md_file.write(f"# Directory structure of {root_dir}\n\n")
            md_file.write("```\n")
            md_file.write(tree_structure)
            md_file.write("```\n")
        logging.info(f"Directory structure exported to {md_filename}")
    except Exception as e:
        logging.error(f"Error exporting to Markdown: {e}")


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

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    root_dir = args.directory
    export_md = args.export_md
    depth = args.depth
    color = args.color

    if not os.path.isdir(root_dir):
        logging.error(
            "The provided path is not a valid directory. Please try again.")
        sys.exit(1)

    logging.info(f"Starting directory scan for: {root_dir}")
    # Disable color mode if exporting to Markdown
    color_mode = color if not export_md else False
    tree_structure, file_count = print_directory_tree(
        root_dir, depth=depth, color_mode=color_mode)
    print(Fore.YELLOW + root_dir if color else root_dir)
    print(tree_structure)
    print(f"\n├──────── [{file_count} files]")

    if export_md:
        export_to_markdown(root_dir, tree_structure)


if __name__ == "__main__":
    main()
