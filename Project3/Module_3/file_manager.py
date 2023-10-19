# Author: Nikhil Saini
# Class: CS325
# Description: The file_manager.py script defines a FileManager class with static methods for managing 
# files and directories in Python. It includes methods for creating directories, and saving text data to files. 
# This script serves as a utility module for handling file-related operations and is particularly useful for 
# organizing and storing data in projects where file and directory management is essential.


import os

class FileManager:
    @staticmethod
    def create_directory(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    def save_text_to_file(text, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8',) as file:
                file.write(text)
            # print(f"File saved: {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the file: {str(e)}")
