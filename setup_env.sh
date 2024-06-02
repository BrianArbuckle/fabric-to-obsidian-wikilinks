#!/bin/bash

# Variables for default configuration paths
ENV_PATH=~/.config/fabric-to-obsidian/.env
DIR_PATH=~/.config/fabric-to-obsidian

# Create directory if it doesn't exist
if [ ! -d "$DIR_PATH" ]; then
  mkdir -p "$DIR_PATH"
  echo "Created directory: $DIR_PATH"
else
  echo "Directory already exists: $DIR_PATH"
fi

# Prompt the user for the paths
read -p "Enter the path for PEOPLE_FOLDER: " PEOPLE_FOLDER
read -p "Enter the path for DOCUMENTS_FOLDER: " DOCUMENTS_FOLDER

# Create .env file and write the paths
echo "PEOPLE_FOLDER=\"$PEOPLE_FOLDER\"" > "$ENV_PATH"
echo "DOCUMENTS_FOLDER=\"$DOCUMENTS_FOLDER\"" >> "$ENV_PATH"

echo ".env file created at $ENV_PATH with the following contents:"
cat "$ENV_PATH"
