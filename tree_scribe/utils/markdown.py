import os
import logging


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
