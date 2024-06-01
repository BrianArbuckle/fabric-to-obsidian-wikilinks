import os
import re
import difflib

from dotenv import load_dotenv

# Constants for the .env file and variable names
DEFAULT_CONFIG = "~/.config/fabric-to-obsidian/.env"
PEOPLE_FOLDER_VAR = "PEOPLE_FOLDER"
DOCUMENTS_FOLDER_VAR = "DOCUMENTS_FOLDER"

# Load environment variables from the .env file
load_dotenv(os.path.expanduser(DEFAULT_CONFIG))

# Retrieve the folder paths from environment variables
people_folder = os.getenv(PEOPLE_FOLDER_VAR)
documents_folder = os.getenv(DOCUMENTS_FOLDER_VAR)

# Function to get a list of people from the people folder
def get_people_list(people_folder):
    people = []
    for filename in os.listdir(people_folder):
        if filename.endswith(".md"):
            person_name = os.path.splitext(filename)[0]
            people.append(person_name)
    return people

# Function to replace names in the document with Obsidian links
def link_names_in_doc(filepath, people_list):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # First pass: Replace full names
    for person in sorted(people_list, key=lambda x: -len(x)):  # Sort by length to replace longer names first
        pattern = fr"\b{re.escape(person)}\b"
        linked_name = f"[[{person}]]"
        content = re.sub(pattern, linked_name, content)

    # Second pass: Replace partial names only if not inside existing links
    for person in sorted(people_list, key=lambda x: -len(x)):
        first_name = person.split()[0]
        pattern = fr"(?<!\[\[){re.escape(first_name)}\b(?!\]\])"
        linked_name = f"[[{person}|{first_name}]]"
        content = re.sub(pattern, linked_name, content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    people_list = get_people_list(people_folder)

    for doc in os.listdir(documents_folder):
        if doc.endswith(".md"):
            print(f"Processing {doc}")
            doc_path = os.path.join(documents_folder, doc)
            link_names_in_doc(doc_path, people_list)


if __name__ == "__main__":
    main()
