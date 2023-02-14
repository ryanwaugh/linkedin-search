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
parser.add_argument('-d', '--debug', action='store_true', help='Enable raw output dump')

args = parser.parse_args()
title = args.title.replace(' ', '%20')
location = args.location.replace(' ', '%20')
url = f'https://www.linkedin.com/jobs/search?keywords={title}&location={location}'

with HTMLSession() as session:
    response = session.get(url)

soup = BeautifulSoup(response.text, 'lxml')
results = soup.find(id='main-content')
# jobs = results.find_all('div', class_='result-card__contents job-result-card__contents')
jobs = results.find('section', class_='two-pane-serp-page__results-list')
jobs_list = jobs.find_all('li')

if args.debug is not False:
    print(jobs_list)
else:
    print("LinkedIn webpage changed, service not working at the moment : (")
    print("hint: use --debug to enable raw output dump")

# for listing in jobs:
#     title = listing.find('h3', class_='result-card__title job-result-card__title')
#     company = listing.find('h4', class_='result-card__subtitle job-result-card__subtitle')
#     location = listing.find('span', class_='job-result-card__location')
#     print(title.text.strip())
#     print(company.text.strip())
#     print(location.text.strip())
#     print()
