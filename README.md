# Fabric to Obsidian Wikilinks

A utility to create appropriately named Wikilinks within markdown documents.

This is derived from my specific use case of adding [fabric](https://github.com/danielmiessler/fabric)-generated markdown files directly into my Obsidian `Inbox/fabric` vault. I initially played around with editing the fabric patterns to add the double brackets `[[ ]]` around names extracted from my Obsidian folder `People (and Companies)`. This became a much larger project, explicitly writing some Python code to do the work post-fabric generation. was a more elegant solution (IMHO).

I could see this or a generalized version of this project incorporated into the fabric `save.py` file with a flag to call the code.


## Setup Script for fabric-to-obsidian

This repository contains a setup script to create the necessary `.env` file for configuring your paths.

## Running the setup script

### Unix-based Systems (Linux, macOS)

1. Clone the repository:

    ```sh
    git clone git@github.com:BrianArbuckle/fabric-to-obsidian-clean-up.git
    cd fabric-to-obsidian
    ```

2. Run the setup script:

    ```sh
    sh setup_env.sh
    ```

    Alternatively, you can make the script executable and run it:

    ```sh
    chmod +x setup_env.sh
    ./setup_env.sh
    ```

### Windows Systems

For Windows users, it's recommended to run the script in a WSL environment, or you can manually create the `.env` file under the specified directory with the following contents.

```plaintext
# .env
PEOPLE_FOLDER="your/path/to/people_folder"
DOCUMENTS_FOLDER="your/path/to/documents_folder"
```

## Running the Python scritp:

### Step 1: Install Dependencies

Once you have Poetry installed, navigate to your project directory and install the dependencies:

```sh
poetry install
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment created by Poetry:

```sh
poetry shell
```

Alternatively, you can run commands within the virtual environment using `poetry run`:

```sh
poetry run python main.py
```

### Step 3: Run the Script

Now you can run the main script:

```sh
python main.py
```
