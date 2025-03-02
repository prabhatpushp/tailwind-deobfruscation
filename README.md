# Tailwind CSS Deobfuscation

## Introduction
This project provides functionality to deobfuscate Tailwind CSS class definitions by hashing their content. It extracts class definitions from a Tailwind CSS file, generates SHA-256 hashes for their content, and saves the mappings to a JSON file for easy reference.

## Features
- **CSS Class Extraction**: Automatically extracts CSS class definitions from a Tailwind CSS file.
- **Hash Mapping**: Generates SHA-256 hashes for class content and maps them to their respective class names.
- **JSON Output**: Saves the hash mappings to a JSON file for easy access and analysis.

## Tech Stack
- **Python**: The implementation is written in Python.
- **Hashlib**: Used for generating SHA-256 hashes.
- **Regular Expressions**: Utilized for extracting CSS class definitions.
- **JSON**: For saving the hash mappings.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/prabhatpushp/tailwind-deobfruscation
   cd tailwind deobfruscation
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To use the Tailwind deobfuscation functionality, you can run the `main.py` script. Here is an example:
```python
from main import hash_css_classes

# Run the main function to generate hash mappings
if __name__ == '__main__':
    main()
```
This will read the `originalTailwind.txt` file, generate hash mappings, and save them to `hash_mapping.json`.

## Development
- The main implementation is in `main.py`. You can modify or extend the functionality as needed.
- Ensure to test your changes thoroughly to maintain the integrity of the deobfuscation process.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes and create a pull request.

## License
This project is licensed under the MIT License. Feel free to use this project for personal or commercial purposes. 
