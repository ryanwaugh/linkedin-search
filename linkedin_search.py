# linkedin_search.py
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

title = input ("Enter the job title you wish to search for : ") 
location = input("Enter the job location you wish to search for : ")

title = title.replace(' ', '%20')
location = location.replace(' ', '%20')

url = 'https://www.linkedin.com/jobs/search?keywords=' + title + '&location=' + location
try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find(id='main-content')
jobs = results.find_all('div', class_='result-card__contents job-result-card__contents')

for listing in jobs:
    title = listing.find('h3', class_='result-card__title job-result-card__title')
    company = listing.find('h4', class_='result-card__subtitle job-result-card__subtitle')
    location = listing.find('span', class_='job-result-card__location')
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()