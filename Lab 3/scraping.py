from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up WebDriver service
service = Service(
    executable_path="C:\\Users\\musno\\OneDrive\\Desktop\\SEMESTER 3\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
)

# Configure Chrome options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store scraped data
products = []  # List to store drama names
episodes = []  # List to store episode counts
times = []  # List to store release times

# Navigate to the page
driver.get("https://dramacool.sh/category/latest-asian-drama-releases/")

# Wait for the page to load specific elements
wait = WebDriverWait(driver, 10)

    
    # Once the page is loaded, get the page source
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

    # Find all list items with the class "mask"
for a in soup.findAll("li", attrs={"class": "mask"}):
    name = a.find("h3")  # Drama name
    episode = a.find("span", attrs={"class": "ep sub"})  # Episode count
    times_element = a.find("span", attrs={"class": "time"})  # Time element

        # Check if the elements exist
    if name and episode and times_element:
        print(f"Drama: {name.text.strip()}, Episode: {episode.text.strip()}, Time: {times_element.text.strip()}")
        products.append(name.text.strip())  # Append drama name
        episodes.append(episode.text.strip())  # Append episode count
        times.append(times_element.text.strip())  # Append time info
        
        # Stop after scraping 50 items
    if len(products) == 50:
        break


# Create a pandas DataFrame and save to CSV
df = pd.DataFrame({"Drama Name": products, "Episodes": episodes, "Release Time": times})
df.to_csv("dramas.csv", index=False, encoding="utf-8")

# Close the browser
driver.quit()


#---------------------------------------------------------------------------


# Set up Chrome WebDriver
service = Service(
    executable_path="C:\\Users\musno\OneDrive\Desktop\SEMESTER 3\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store data
titles = []
episodesNumbers = []
imageAddresses = []
updatedTime = []
episodeLinks = []

# Visit the Dramacool website
driver.get("https://dramacool.sh/")
time.sleep(5) 


content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

# Scrape data
for box in soup.findAll("ul", attrs={"class": "box"}):
    for li in box.findAll("li"):
        titleTag = li.find("h3")
        episodeTag = li.find("span", class_="ep raw")
        timeTag = li.find("span", class_="time")
        imageTag = li.find("img")
        linkTag = li.find("a", class_="mask")
        
        # Extract and append data
        if titleTag and episodeTag and timeTag and imageTag and linkTag:
            titles.append(titleTag.text.strip())
            episodesNumbers.append(episodeTag.text.strip())
            updatedTime.append(timeTag.text.strip())
            imageAddresses.append(imageTag['src'])
            episodeLinks.append(linkTag['href'])

# Create a DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Episode": episodesNumbers,
    "Image URL": imageAddresses,
    "Time": updatedTime,
    "Episode Link": episodeLinks
})

# Save to CSV
df.to_csv("Kdramas.csv", index=False, encoding="utf-8")

# Close the browser
driver.quit()

print("Scraping completed and data saved to 'dramacool_episodes.csv'.")


#--------------------------------------------------------------------------

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

#---------------------------------------------------------------


# Navigate to the page
driver.get("https://www.nike.com/w/mens-shoes")

# Give the page some time to load (in case it's dynamic)
time.sleep(5)

# Parse page content with BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# Find all product cards and extract information
for div in soup.findAll("div", attrs={"class": "product-card"}):
    name = div.find("div", attrs={"class": "product-card__title"})
    desc = div.find("div", attrs={"class": "product-card__subtitle"})
    colours = div.find("div", attrs={"class": "product-card__product-count"})
    price = div.find("div", attrs={"class": "product-price"})
    
    # Check if all the necessary fields are present
    if name and desc and colours and price:
        products.append(name.text)
        types.append(desc.text)
        noOfColours.append(colours.text.strip())  # Store the number of colors
        prices.append(price.text.strip())  # Store the price
    
    # Stop after 50 products
    if len(products) == 50:
        break

# Create a pandas DataFrame and save to CSV
df = pd.DataFrame({"Product Name": products, "Price": prices, "No Of Colours": noOfColours, "Types": types})
df.to_csv("nike.csv", index=False, encoding="utf-8")

# Close the browser
driver.quit()


#-------------------------------------------------------------


service = Service(
    executable_path="C:\\Users\musno\OneDrive\Desktop\SEMESTER 3\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')

products = []  # List to store name of the product
prices = []  # List to store price of the product
# ratings = []  # List to store rating of the product

driver.get("https://www.whatmobile.com.pk/")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("li", attrs={"class": "product"}):
    print(a)
    name = a.find("a", attrs={"class": "BiggerText"})
    price = a.find("span", attrs={"class": "PriceFont"})
    if name != None and price != None:
        products.append(name["title"])
        prices.append(price.text)
    if len(products) == 50:
        break

df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("product.csv", index=False, encoding="utf-8")

#-------------------------------------------------------------------


driver.get("https://www.goodreads.com/list/show/1.Best_Books_Ever")
time.sleep(5)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

book_titles = []
authors = []
ratings = []
links = []
image_urls = []

for book in soup.findAll("tr", attrs={"itemtype": "http://schema.org/Book"}):
    title = book.find("a", class_="bookTitle").text.strip()
    author = book.find("a", class_="authorName").text.strip()
    rating = book.find("span", class_="minirating").text.strip()
    link = "https://www.goodreads.com" + book.find("a", class_="bookTitle")['href']
    image_url = book.find("img")['src']
    
    book_titles.append(title)
    authors.append(author)
    ratings.append(rating)
    links.append(link)
    image_urls.append(image_url)

df_goodreads = pd.DataFrame({
    "Book Title": book_titles,
    "Author": authors,
    "Rating": ratings,
    "Link": links,
    "Image URL": image_urls
})
df_goodreads.to_csv("goodreads_books.csv", index=False)

#-------------------------------------------------------------