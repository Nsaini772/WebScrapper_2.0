import requests
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, url):
        self.url = url

    def extract_user_comments(self):
        try:
            # Fetch HTML content from the URL
            response = requests.get(self.url)

            if response.status_code == 200:
                html_content = response.text
                soup = BeautifulSoup(html_content, "html.parser")

                all_data=soup.get_text()
                # Find elements with class 'usertext-body' to extract user comments
                usertext_body_elements = soup.find_all("div",class_='usertext-body')

                user_comments = []
                # print(len(usertext_body_elements)):- done for checking purpose
                for elements in usertext_body_elements:
                    comments = elements.find_all('p')
                    comment_texts = [comment.get_text() for comment in comments]
                    user_comments.extend(comment_texts)

                comments_text = '\n'.join(user_comments)



                # Add debug prints
                # print("Number of usertext-body elements found:", len(usertext_body_elements))
                # print("Number of comments found:", len(user_comments))

                return comments_text
            else:
                print(f"Failed to retrieve content from {self.url}. Status code: {response.status_code}")
                return ""
                
        except Exception as e:
            print(f"An error occurred while extracting user comments: {str(e)}")
            return ""
            
