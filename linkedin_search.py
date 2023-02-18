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
    title = listing.select_one('h3.base-search-card__title').text.strip()
    company = listing.select_one('a.hidden-nested-link').text.strip()
    location = listing.select_one('span.job-search-card__location').text.strip()
    date = listing.select_one('time.job-search-card__listdate').text.strip()
    print(title)
    print(company)
    print(location)
    print(date)
    print()
