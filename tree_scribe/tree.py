import os
import logging
from tree_scribe.utils.helpers import format_size, calculate_folder_size

# Global set to track visited directories
visited_directories = set()


def print_directory_tree(root_dir, indent="", depth=None, current_depth=0, color_mode=False, show_size=False):
    """
    Generate and print the directory tree structure.

    Args:
        root_dir (str): The root directory to start the tree.
        indent (str): Indentation for the current level.
        depth (int): Maximum depth of traversal. None for unlimited.
        current_depth (int): Current traversal depth.
        color_mode (bool): Enable colorful output.
        show_size (bool): Display file sizes and line counts.

    Returns:
        tuple: (tree_structure, file_count) where `tree_structure` is the 
               generated tree as a string, and `file_count` is the number of files.
    """
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
                 if not (os.path.isdir(os.path.join(root_dir, item)) and item in {"node_modules", ".git", "__pycache__"})]
    except PermissionError as e:
        logging.error(f"Permission denied: {root_dir}")
        return "", 0
    except Exception as e:
        logging.error(f"Error reading directory {root_dir}: {e}")
        return "", 0

    # Colors setup for color mode
    dir_color, file_color, size_color, reset_color = ('', '', '', '')
    if color_mode:
        from colorama import Fore, Style
        dir_color = Fore.GREEN
        file_color = Fore.CYAN
        size_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL

    tree_structure = ""
    file_count = 0

    for index, item in enumerate(items):
        path = os.path.join(root_dir, item)
        is_last = index == len(items) - 1

        if os.path.isdir(path):
            # Directory case
            folder_size = calculate_folder_size(path) if show_size else 0
            size_str = f"{size_color}({format_size(folder_size)}){reset_color}" if show_size else ""
            tree_structure += f"{indent}├── {dir_color}{item}/ {size_str}{reset_color}\n" if not is_last else f"{indent}└── {dir_color}{item}/ {size_str}{reset_color}\n"
            new_indent = indent + ("│   " if not is_last else "    ")
            subdir_structure, subdir_file_count = print_directory_tree(
                path, new_indent, depth, current_depth + 1, color_mode, show_size)
            tree_structure += subdir_structure
            file_count += subdir_file_count
        else:
            # File case
            line_info = ""
            if show_size:
                try:
                    file_size = os.path.getsize(path)
                    file_size_str = format_size(file_size)
                    # Count lines in text files
                    with open(path, "r", encoding="utf-8", errors="ignore") as file:
                        line_count = sum(1 for _ in file)
                    line_info = f"{size_color}({line_count} lines, {file_size_str}){reset_color}"
                except Exception as e:
                    logging.debug(f"Error reading file {path}: {e}")
                    line_info = f"{size_color}(Unreadable){reset_color}"

            tree_structure += f"{indent}├── {file_color}{item} {line_info}{reset_color}\n" if not is_last else f"{indent}└── {file_color}{item} {line_info}{reset_color}\n"
            file_count += 1

    return tree_structure, file_count
