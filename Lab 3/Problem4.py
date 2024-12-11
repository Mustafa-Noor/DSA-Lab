from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service(executable_path="C:\\Users\\musno\\OneDrive\\Desktop\\SEMESTER 3\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=options)

course_data = []

driver.get("http://eduko.spikotech.com/Course")

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card")))

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for card in soup.findAll("div", class_="card"):
    title = card.find("h4", class_="card-title").text.strip()
    instructor = card.find_all("h7")[0].text.strip()
    semester = card.find_all("h7")[1].text.strip()
    description = card.find("p", class_="card-text").text.strip()
    
    course_link = card.find("a")["href"]
    driver.get(f"http://eduko.spikotech.com{course_link}")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "details-class")))
    
    details_content = driver.page_source
    details_soup = BeautifulSoup(details_content, features="html.parser")
    
    course_code = "COURSE_CODE"
    CLO1 = CLO2 = CLO3 = CLO4 = "N/A"
    TextBook1 = TextBook2 = "N/A"

    course_data.append([course_code, title, description, CLO1, CLO2, CLO3, CLO4, TextBook1, TextBook2, instructor, semester])
    
    driver.back()

df = pd.DataFrame(course_data, columns=["CourseCode", "Title", "Description", "CLO1", "CLO2", "CLO3", "CLO4", "TextBook1", "TextBook2", "Instructor", "Semester"])
df.to_csv("courses.csv", index=False, encoding="utf-8")

driver.quit()
