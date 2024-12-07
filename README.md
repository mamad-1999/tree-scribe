# Directory Tree Script

This script generates a visual representation of the directory structure of a specified root directory. It supports exporting the structure to a Markdown file and offers various options to customize the output.

### Example Output

```
├── .env
├── .gitignore
├── README.md
├── config/
│   ├── env.go
├── data/
│   ├── found-url.json
│   ├── url.txt
├── db/
│   ├── db.go
├── directory_structure.md
├── go.mod
├── go.sum
├── main.go
├── rss/
│   ├── fetch.go
├── telegram/
│   ├── telegram.go
├── utils/
    ├── http.go
    ├── utils.go
```

## Features

- **Visual Directory Tree**: Display the directory structure in a tree-like format.
- **Export to Markdown**: Save the directory structure to a Markdown file for documentation purposes.
- **Depth Limiting**: Limit the depth of directory traversal to avoid overwhelming outputs for deep directory structures.
- **Colorful Output**: Colorize the terminal output to differentiate directories from files.

## Installation

```bash
 pip install tree-scribe
```
```bash
 pipx install tree-scribe
```

## Command-Line Switches

| Switch/Option            | Description                                                     | Example Usage                       |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------- |
| `<directory-path>`       | Path to the root directory whose structure you want to display. | `tree-scribe /home/project`      |
| `-md`, `--export-md`     | Export the directory structure to a Markdown file.              | `tree-scribe /home/project -md`  |
| `-d`, `--depth <number>` | Limit the depth of directory traversal.                         | `tree-scribe /home/project -d 2` |
| `-v`, `--verbose`        | Enable verbose logging for detailed output.                     | `tree-scribe /home/project -v`   |
| `-c`, `--color`          | Enable colorful output in the terminal.                         | `tree-scribe /home/project -c`   |

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

6. **Combine Options**

   ```bash
   tree-scribe /home/project --export-md --depth 3 -c
   ```

### Notes

- **Colorful Output**: The `-c` or `--color` switch enables colorful terminal output using `colorama`. Without this switch, the output will be plain text.
- **Depth Limiting**: Use the `--depth` option to control how many levels deep the directory tree should be displayed.
- **Verbose Mode**: The `--verbose` option provides more detailed logging information during script execution.
- **Markdown Export**: The `--export-md` option saves the directory structure to a Markdown file for documentation purposes.

For any additional options or troubleshooting, please refer to the [Troubleshooting](#troubleshooting) section of this documentation.

### Troubleshooting

- Permission Errors: If you encounter permission errors, make sure you have the necessary permissions to access the directories and files.
- Invalid Directory Path: Ensure the specified directory path is correct and exists.

### License

This script is provided under the MIT License. See the LICENSE file for more information.

### Contributing

Feel free to submit issues, suggestions, or pull requests. Contributions are welcome!

##### Summary of Additions

- **Customizing Filters**: Instructions for modifying the `filters.py` file to include or exclude specific directories from the output.
- **Adding/Removing Folders**: Clear steps on how to update the `EXCLUDED_DIRECTORIES` list.
