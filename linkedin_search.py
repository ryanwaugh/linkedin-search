## linkedin_search.py
#
# Searches job listings using bs4
# and scraping LinkedIn webpage
#
import requests
import argparse
from requests_html import HTMLSession
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Search for jobs on LinkedIn')
parser.add_argument('-t', '--title', type=str, help='job title of interest')
parser.add_argument('-l', '--location', type=str, help='location of interest')

args = parser.parse_args()
title = args.title.replace(' ', '%20')
location = args.location.replace(' ', '%20')
url = f'https://www.linkedin.com/jobs/search?keywords={title}&location={location}'

with HTMLSession() as session:
    response = session.get(url)

soup = BeautifulSoup(response.text, 'lxml')
results = soup.find(id='main-content')
jobs = results.find('section', class_='two-pane-serp-page__results-list')
jobs_list = jobs.find_all('li')

for listing in jobs_list:
    title = listing.find('h3', class_='base-search-card__title')
    company = listing.find('a', class_='hidden-nested-link')
    location = listing.find('span', class_='job-search-card__location')
    date = listing.find('time', class_='job-search-card__listdate')
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(date.text.strip())
    print()
