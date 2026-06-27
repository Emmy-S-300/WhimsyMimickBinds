#function that takes file_path as input
def read_html_file(file_path):
    
    #open the file_path in read mode using the utf=8 encoding
    with open(file_path, "r", encoding="utf-8") as file:
        
        #read the entire contens of the file and turn it into a string.
        html_content = file.read()

    #returns the html string
    return html_content

#test the function by storing the returned hmtl in the variable html
html = read_html_file("sample.html")

#printing the first 500 chars of the content
print(html[:500])