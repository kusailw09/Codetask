import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Fetch the page
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Example: Extract all headings (h1 tags)
for heading in soup.find_all("h1"):
    print(heading.text.strip())
