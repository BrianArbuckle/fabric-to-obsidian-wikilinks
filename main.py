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
def get_people_list(people_folder: str) -> list[str]:
    """
    Retrieves a list of people from the specified folder.

    Args:
        people_folder (str): The path to the folder containing the markdown files of people.

    Returns:
        list[str]: A list of people's names derived from the filenames in the given folder.
    """
    people = []
    for filename in os.listdir(people_folder):
        if filename.endswith(".md"):
            person_name = os.path.splitext(filename)[0]
            people.append(person_name)
    return people

# Function to replace names in the document with Obsidian links
def link_names_in_doc(filepath: str, people_list: list[str]) -> None:
    """
    Replaces names in the specified document with Obsidian links.

    Args:
        filepath (str): The path to the document where names need to be linked.
        people_list (list[str]): A list of people's names to be linked in the document.

    Returns:
        None
    """
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

def main() -> None:
    """
    Processes all markdown documents in the 'documents_folder' by linking names from 'people_folder'.

    TODO: Implement difflib for close matches, and handle cases where the first name is not unique.

    Args:
        None

    Returns:
        None
    """
    
    people_list = get_people_list(people_folder)

    for doc in os.listdir(documents_folder):
        if doc.endswith(".md"):
            print(f"Processing {doc}")
            doc_path = os.path.join(documents_folder, doc)
            link_names_in_doc(doc_path, people_list)

if __name__ == "__main__":
    main()
