import os
import logging


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
