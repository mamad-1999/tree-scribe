# Directory Tree Script

This script generates a visual representation of the directory structure of a specified root directory. It supports exporting the structure to a Markdown file and offers various options to customize the output.

```
Usage: tree-script [SWITCHES] directory

Generate a directory tree structure for a given path, with options for depth
limitation, colorful output, file sizes, and exporting to Markdown.

positional arguments:
  directory             Path to the root directory to analyze

optional arguments:
  -h, --help            Show this help message and exit
  -md, --export-md      Export the directory structure to a Markdown file
  -d DEPTH, --depth DEPTH
                        Limit the depth of directory traversal (e.g., -d 2)
  -v, --verbose         Enable verbose logging for debugging purposes
  -c, --color           Enable colorful output for better readability
  -s, --size            Show file sizes and line counts in the output

Examples:
  tree-script /path/to/directory
  tree-script /path/to/directory -d 2 -s
  tree-script /path/to/directory -md -c
```

### Example Output

![-d](https://github.com/user-attachments/assets/dea8ad31-55ae-4658-9ccd-06074719c769)

## Installation

```bash
 pip install tree-scribe
```

Or

```bash
 pipx install tree-scribe
```

## Command-Line Switches

| Switch/Option            | Description                                                     | Example Usage                                              |
| ------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------- |
| `<directory-path>`       | Path to the root directory whose structure you want to display. | `tree-scribe /home/project`                                |
| `-md`, `--export-md`     | Export the directory structure to a Markdown file.              | `tree-scribe /home/project -md`                            |
| `-d`, `--depth <number>` | Limit the depth of directory traversal.                         | `tree-scribe /home/project -d 2`                           |
| `-v`, `--verbose`        | Enable verbose logging for detailed output.                     | `tree-scribe /home/project -v`                             |
| `-c`, `--color`          | Enable colorful output in the terminal.                         | `tree-scribe /home/project -c`                             |
| `-s`, `--size`           | Show line and size.                                             | `tree-scribe /home/project -s`                             |
| `--exclude`              | Exclude file and folder.                                        | `tree_scribe /path/to/directory --exclude dist build .git` |

## Examples

1. **Display the Directory Structure**

   ```bash
   tree-scribe /home/project
   ```

2. **Export to Markdown**

   ```bash
   tree-scribe /home/project --export-md
   ```

3. **Limit Depth to 2 Levels**

   ```bash
   tree-scribe /home/project --depth 2
   ```

4. **Enable Verbose Logging**

   ```bash
   tree-scribe /home/project --verbose
   ```

5. **Enable Colorful Output**

   ```bash
   tree-scribe /home/project -c
   ```

6. **Show line and size**

   ```bash
   tree-scribe /home/project -s
   ```

7. **Combine Options**

   ```bash
   tree-scribe /home/project --export-md --depth 3 -c -s
   ```

8. **Exclude files or folder**

   ```bash
   tree_scribe /path/to/directory --exclude dist build .git
   ```

### Troubleshooting

- Permission Errors: If you encounter permission errors, make sure you have the necessary permissions to access the directories and files.
- Invalid Directory Path: Ensure the specified directory path is correct and exists.

### License

This script is provided under the MIT License. See the LICENSE file for more information.

### Contributing

Feel free to submit issues, suggestions, or pull requests. Contributions are welcome!
