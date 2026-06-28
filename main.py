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

    #create a dictionary to store story data in
    story_data = {
        "title": "",
        "author":"",
        "chapters":[],
        }
   
    #find the 1st h1 elemnt and extract only its text
    story_title = soup.find("h1").get_text(strip=True)
    #add title to the dictionary
    story_data["title"] = story_title

    # find the author and extract only the text
    story_author = soup.find("a", {"rel": "author"}).get_text(strip=True)
    #add the author to the dictionary
    story_data["author"] = story_author



    #return the dictionary
    return story_data

    

# read the sample html
html = read_html_file("sample.html")

#parse the html
parse_story_html(html)

#store the dictionary in a variable
story = parse_story_html(html)

print(story)