import requests
from Module_2.html_parser import HTMLParser

class DataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                print("response.text not working")
                return None
        except Exception as e:
            print(f"An error occurred while fetching data: {str(e)}")
            return None

    def save_data(self, data, output_file):
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while saving data: {str(e)}")
