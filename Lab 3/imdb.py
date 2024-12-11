from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome WebDriver
service = Service(
    executable_path="C:\\Users\musno\OneDrive\Desktop\SEMESTER 3\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# IMDb scraping
driver.get("https://www.imdb.com/chart/top/")
time.sleep(5)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

# Lists for IMDb data
titles = []
years = []
ratings = []
genres = []
links = []

for movie in soup.findAll("td", attrs={"class": "titleColumn"}):
    title = movie.a.text.strip()
    year = movie.span.text.strip("()")
    link = "https://www.imdb.com" + movie.a['href']
    titles.append(title)
    years.append(year)
    links.append(link)

for movie in soup.findAll("td", attrs={"class": "ratingColumn imdbRating"}):
    rating = movie.strong.text.strip()
    ratings.append(rating)

# Adding genres manually or via individual movie links
# This part would require visiting each movie page for full genre extraction, omitted for brevity

df_imdb = pd.DataFrame({
    "Title": titles,
    "Year": years,
    "Rating": ratings,
    "Link": links
})
df_imdb.to_csv("imdb_movies.csv", index=False)
