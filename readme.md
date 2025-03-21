# ChadGPT Terminal

A natural language terminal interface that converts your everyday language into terminal commands.

## Features

- Natural language input for terminal commands
- Beautiful terminal interface with colored output
- Powered by OpenAI's GPT-3.5
- Safe command execution with error handling

## Installation

You can install ChadGPT Terminal using pip:

```bash
pip install chadgpt
```

## Usage

After installation, you can run ChadGPT Terminal in two ways:

1. Using the command-line tool:
```bash
chadgpt
```

2. Using Python:
```python
from chadgpt.cli import main
main()
```

Then simply type your requests in natural language. For example:
- "list all files in the current directory"
- "show me the size of all files in descending order"
- "create a new directory called projects"
- "find all Python files in the current directory"

Type 'exit' or 'quit' to close the application.

## Examples

```
What would you like to do? list all files with their sizes in ascending order
Executing command: ls -lh | sort -k5 -n
```

```
What would you like to do? find all Python files in the current directory
Executing command: find . -name "*.py"
```

## Development

If you want to contribute to the project:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chadgpt.git
cd chadgpt
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Make your changes and submit a pull request!

## Safety Note

The application uses OpenAI's GPT-3.5 to convert natural language to commands. While it's designed to be safe, always review the generated command before execution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
