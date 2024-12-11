# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
# from selenium.webdriver.chrome.service import Service
# import time as sleep

# # webdriver can be downloaded from
# #https://sites.google.com/chromium.org/driver/downloads/versionselection?authuser=0

# service = Service(
#     executable_path="C:\\Users\musno\OneDrive\Desktop\SEMESTER 3\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# )
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
# # driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')

# products = []  # List to store name of the product
# types = [] # 
# prices = []  # List to store price of the product
# noOfColours = []  # List to store rating of the product

# driver.get("https://www.nike.com/w/mens-shoes")

# content = driver.page_source

# soup = BeautifulSoup(content, features="html.parser")
# # print(soup)
# for div in soup.findAll("div", attrs={"class": "product-card"}):
    
#     name = div.find("div", attrs={"class": "product-card__title"})
#     desc = div.find("div", attrs={"class": "product-card__subtitle"})
#     colours = div.find("div", attrs={"class": "product-card__product-count"})
#     price = div.find("div", attrs={"class": "product-price"})
#     if name != None and price != None and desc != None and colours != None:
#         products.append(name.text)
#         types.append(desc.text)
#         colours.append(colours.text)
#         price.append(price.text)
#     if len(products) == 50:
#         break

# df = pd.DataFrame({"Product Name": products, "Price": prices, "No Of Colours": noOfColours, "Types": types})
# df.to_csv("nike.csv", index=False, encoding="utf-8")


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

# Path to the chromedriver
service = Service(
    executable_path="C:\\Users\\musno\\OneDrive\\Desktop\\SEMESTER 3\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
)

# Initialize Chrome browser options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store scraped data
products = []  # List to store name of the product
types = []  # List to store the type (e.g., shoe model)
prices = []  # List to store price of the product
noOfColours = []  # List to store number of available colors

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
