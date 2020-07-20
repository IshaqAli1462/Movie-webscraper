import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

soup = BeautifulSoup(r.text, 'html.parser')
movie = []

for item in soup.find_all("td", {"class": "titleColumn"}):
    for i in item.find_all('a'):     
        movie.append(i.text)

print("The Top 10 IMDB movies in decending order:")
for ran in range(0,10):
    print(movie[ran])

