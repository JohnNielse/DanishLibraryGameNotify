import requests
from bs4 import BeautifulSoup



r = requests.get("https://helsbib.dk/search/ting/Playstation%204?&profile=spil")  # Basic login request
soup = BeautifulSoup(r.text, 'lxml')

match = soup.find(class_='search-results ting_search-results')
print (match)
