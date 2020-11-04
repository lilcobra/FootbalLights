import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver

path = r'C:\\Users\\Brad\\Downloads\\chromedriver_win32'
driver = webdriver.Chrome(executable_path = path)
URL = 'https://www.google.com/search?q='
team1 = 'steelers' #get team1
team2 = 'Titans' #get team2
page = requests.get(URL +  team1 + '%20vs%20' + team2)

driver.get(URL +  team1 + '%20vs%20' + team2)

#soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify)

text = driver.find_all
score1 = driver.find_element_by_class_name('imso_mh__l-tm-sc imso_mh__scr-it imso-light-font')
score2 = driver.find_element_by_class_name('imso_mh__r-tm-sc imso_mh__scr-it imso-light-font')

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify)
f = open("sourcecode.txt", "w")
f.write(str(soup.prettify))
f.close()

results = soup.find(id='sports-app')

driver.close()

#print(results.prettify())

#job_elems = results.find_all('section', class_='card-content')

"""
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()"""