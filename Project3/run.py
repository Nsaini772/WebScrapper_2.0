import sys
import os
from Module_1.data_fetcher import DataFetcher
from Module_2.html_parser import HTMLParser
from Module_3.file_manager import FileManager

def main():
    if len(sys.argv) != 2:
        # print("Usage: python run.py URL")
        sys.exit(1)

    url = sys.argv[1]

    # Fetch data
    data_fetcher = DataFetcher(url)
    html_content = data_fetcher.fetch_data()

    if html_content is not None:
        # Extract comments
        html_parser = HTMLParser(url)
        comments_text = html_parser.extract_user_comments()

        # Define the directory paths
        raw_data_directory = "Data/raw"
        processed_data_directory = "Data/processed"

        # # Create directories
        FileManager.create_directory(raw_data_directory)
        FileManager.create_directory(processed_data_directory)

        # File paths
        raw_file_path = os.path.join(raw_data_directory, "raw_data.txt")
        processed_file_path = os.path.join(processed_data_directory, "processed_comments.txt")

        # Save comments in the specified directories
        FileManager.save_text_to_file(html_content, raw_file_path)
        FileManager.save_text_to_file(comments_text, processed_file_path)
        # print(comments_text):- done to check the details
        
        print("User comments extracted and saved")

if __name__ == "__main__":
    main()

# python3 /Users/swastik/Downloads/CS325/Project3/run.py https://old.reddit.com/r/funny/comments/16ke3e5/can_anyone_verify_this_stuff/