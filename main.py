from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "lxml")
title = soup.find_all(name="h3", class_="title")
print(title)

with open("./data/movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed(title):
        print(str(movie.getText()))
        file.write(str(movie.getText()))
        file.write("\n")
