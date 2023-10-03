import sys
from bs4 import BeautifulSoup

def is_user_comment(tag):
    # Define a function to filter elements that are user comments
    if tag.name == 'p':
        # Exclude <p> tags containing links
        return not tag.find_all('a', href=True)
    return False

def extract_user_comments(input_file_path, output_file_path):
    try:
        # Read the input file
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            html_content = input_file.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements with class "usertext-body" (adjust as needed)
        usertext_body_elements = soup.find_all(class_='usertext-body')

        # Initialize an empty list to store user comments
        user_comments = []

        for element in usertext_body_elements:
            # Filter out headings and keep only user comments
            comments = element.find_all(is_user_comment)

            # Extract the text content from user comments
            comment_texts = [comment.get_text() for comment in comments]

            # Join the comment texts into a single string
            user_comments.extend(comment_texts)

        # Join the user comments into a single string
        comments_text = '\n'.join(user_comments)

        # Write the comments to the output file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(comments_text)

        print(f"User comments extracted and saved to {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script_name.py input_file.html output_user_comments.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    extract_user_comments(input_file_path, output_file_path)


# python3 Project2.py output_file1.txt output_file2.txt