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