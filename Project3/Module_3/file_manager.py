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
