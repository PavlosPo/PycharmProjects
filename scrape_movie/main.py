from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, "lxml")
title_movies = [item.getText() for item in soup.find_all(name="h3", class_="title")]

with open("movies.txt", "w") as file:
    file.writelines([title_movie+'\n' for title_movie in title_movies[::-1]])