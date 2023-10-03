# WebScrapper_2.0

input file or dump file from WebScrapper (previous code):- output_file1.txt
refined output file form the WebScrapper_2.0 :- output_file2.txt

yaml file contains the details of all the libraries installed like requests and beautifulsoup4

to run this script:- python3 Project2.py output_file1.txt output_file2.txt
in general:- python3 your_python_script.py input.txt output.txt

In this project I tried to remove the tags fromt eh dump file and stored the user comments as a output file. During this I inspect the website and figure out which tag and class or id contains the user comment data then used that details with soup to extract data. 
I used soup.find_all() method. It's a method provided by the BeautifulSoup object to search and find all instances of a specific HTML element or tag within the parsed HTML content.
And then getting the data from the class "usertext-body".
