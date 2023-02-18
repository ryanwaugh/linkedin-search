## linkedin_search.py
#
# Searches job listings using bs4
# and scraping LinkedIn webpage
#
import requests
import argparse
import sys
from bs4 import BeautifulSoup

# prompt for user input to specify job title & location
parser = argparse.ArgumentParser(description='Search for jobs on LinkedIn')
parser.add_argument('-t', '--title', type=str, help='job title of interest')
parser.add_argument('-l', '--location', type=str, help='location of interest')

args = parser.parse_args()

# only proceed if both arguments present
if args.title is None or args.location is None:
    sys.exit("Job title and/or location not provided!")

# replace spaces in arguments with underscores, for compatibility
title = args.title.replace(' ', '%20')
location = args.location.replace(' ', '%20')
url = f'https://www.linkedin.com/jobs/search?keywords={title}&location={location}'

# init session with parameterized URL
session = requests.Session()
response = session.get(url)

# filter results to list of jobs only
soup = BeautifulSoup(response.text, 'lxml')
results = soup.find(id='main-content')
jobs = results.find('section', class_='two-pane-serp-page__results-list')
jobs_list = jobs.find_all('li')

list_length = len(jobs_list)
print(f"{list_length} jobs found: \n")

# find and print info about each job listing
for listing in jobs_list:
    title = listing.select_one('h3.base-search-card__title')
    company = listing.select_one('a.hidden-nested-link')
    location = listing.select_one('span.job-search-card__location')
    date = listing.select_one('time.job-search-card__listdate')
    if title is not None: 
        print(title.text.strip())
    if company is not None:
        print(company.text.strip())
    if location is not None:
        print(location.text.strip())
    if date is not None:
        print(date.text.strip())
    print()
