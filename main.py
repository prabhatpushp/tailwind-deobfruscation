import hashlib
import re
import json

def hash_css_classes(css_string):
    css_classes = re.findall(r'\.[^\s{}]+(?:\\.[^\s{}]+)* *\{[^}]*\}', css_string)

    hash_mapping = {}

    for css_class in css_classes:
        class_name = re.match(r'\.[^\s{}]+(?:\\.[^\s{}]+)*', css_class).group()[1:]
        class_content = re.search(r'\{([^}]*)\}', css_class).group(1)
        valid_class_name = class_name.split('::')[0].split('[')[0].split(':not')[0].split('+')[0]  # Extracting only the valid class name
        # equivalent to content.replace(/\s/g, "").replace(/\n/g, "").replace(/\t/g, "").replace(/\r/g, "").replace(/\f/g, "").replace(/\v/g, "");
        class_content = re.sub(r'\s|\n|\t|\r|\f|\v', '', class_content)
        hash_value = hashlib.sha256(class_content.encode()).hexdigest()
        hash_mapping[hash_value] = valid_class_name

    return hash_mapping

def main():
    with open('originalTailwind.txt', 'r') as file:
        css_content = file.read()

    hash_mapping = hash_css_classes(css_content)

    with open('hash_mapping.json', 'w') as json_file:
        json.dump(hash_mapping, json_file, indent=4)

if __name__ == "__main__":
    main()
