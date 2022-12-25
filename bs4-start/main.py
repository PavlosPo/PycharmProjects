from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://news.ycombinator.com")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "lxml")


article_tags = [link.find("a") for link in soup.find_all(name="span", class_="titleline")]
article_texts = []
article_links = []
for article_tag in article_tags:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

# Get the maximum number's index.
maximum = max(article_upvotes)
maximum_index = article_upvotes.index(maximum)
print(article_texts[maximum_index], article_links[maximum_index])




































































# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")

# print(soup.title)

# print(soup.title.string)
# print(soup.prettify())


# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")  # id named name
# print(name)
#
#
# headings = soup.select(selector=".heading")  # class named heading
# print(headings)

