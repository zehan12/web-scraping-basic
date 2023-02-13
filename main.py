import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("h1").text
first_paragraph = soup.find("h3").text
link = soup.find_all("a")

print(title)
print(first_paragraph)


for l in link:
    print(l.get("href"))
