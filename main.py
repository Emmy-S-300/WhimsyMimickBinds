# from this library, import the beautifulsoup class
from bs4 import BeautifulSoup


#function that takes file_path as input
def read_html_file(file_path):
    
    #open the file_path in read mode using the utf=8 encoding
    with open(file_path, "r", encoding="utf-8") as file:
        
        #read the entire contens of the file and turn it into a string.
        html_content = file.read()

    #returns the html string
    return html_content

#Convert the html string into something python can search through.
def parse_story_html(html_content):
    #Use BeautifulSoup to parse the html and create a searchable object
    soup = BeautifulSoup(html_content, "html.parser")

    #find the 1st h1 elemnt and extract only its text
    title = soup.find("h1").get_text(strip=True)

    #print the variable
    print(title)

# read the sample html
html = read_html_file("sample.html")
#parse the html
parse_story_html(html)