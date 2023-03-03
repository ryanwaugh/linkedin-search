## linkedin_search.py
#
# Searches job listings on 
# LinkedIn, using bs4
# to scraping the webpage
#
import requests
import argparse
import sys
from bs4 import BeautifulSoup

def populateJobsList(url, current_session):
    try:
        response = current_session.get(url)
        # allow for HTTPError to be raised
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # cleanly print HTTP error codes
        raise SystemExit(err)
    except requests.exceptions.RequestException as e:
        # all other exceptions
        raise SystemExit(e)

    # use lxml parser to get main contents
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find(id='main-content')
    # select class containing relavant listings
    jobs = results.find('section', class_='two-pane-serp-page__results-list')
    # filter results to list of jobs only
    jobs_list = jobs.find_all('li')

    # print info about each job listing
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

    print(len(jobs_list), "jobs found.")

# prompt for user input to specify job title & location
parser = argparse.ArgumentParser(description='Search for jobs on LinkedIn')
parser.add_argument('-t', '--title', type=str, help='job title of interest')
parser.add_argument('-l', '--location', type=str, help='location of interest')

args = parser.parse_args()

# only proceed if a title is provided
if args.title is not None:
    title =  args.title.replace(' ', '%20')
    if args.location is not None:
        # search w/ both title & location:
        location = args.location.replace(' ', '%20')
        url_string = f'https://www.linkedin.com/jobs/search?keywords={title}&location={location}'
    else:
        # search w/ title only:
        url_string = f'https://www.linkedin.com/jobs/search?keywords={title}'
else:
    if args.location is None:
        sys.exit(f'Error: Please provide a job title and (optional) location')
    else:
        sys.exit(f'Error: Please provide a job title to search for in "{args.location}"')

page = requests.Session()
populateJobsList(url_string, page)
page.close()
