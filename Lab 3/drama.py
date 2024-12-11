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

    # Wait until at least one "mask" element is present in the DOM
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mask")))
    
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
