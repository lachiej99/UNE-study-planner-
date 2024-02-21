import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://handbook.une.edu.au/search"

# Make a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor elements with the specified class
    print(soup)
    course_links = soup.find_all('a', class_='css-1flav9m-results-styles--StyledLink e1ecnqs54')
    print(course_links)
    # Extract the URLs from the anchor elements
    course_urls = [link['href'] for link in course_links]
    # Print the list of course URLs
    print(course_urls)
else:
    print("Error:", response.status_code)


from bs4 import BeautifulSoup

# Sample HTML snippet
html_snippet = '<a href="/units/2024/AFM211" class="css-1flav9m-results-styles--StyledLink e1ecnqs54"><span class="result-item-title"><span><span class="">AFM211 Intermediate Financial Accounting</span></span></span><div class="result-item-content1">Unit | All</div></a>'

# Parse the HTML snippet
soup = BeautifulSoup(html_snippet, 'html.parser')

# Find the <a> tag
a_tag = soup.find('a')

# Extract the value of the 'href' attribute
href_value = a_tag['href']

# Split the href value by '/' and get the unit code
unit_code = href_value.split('/')[-1]

print("Unit Code:", unit_code)

