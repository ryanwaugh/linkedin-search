# LinkedIn Job Search

A simple program allowing you to search LinkedIn for job opportunities based on job title and location. It uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to scrape job listings from LinkedIn's job search page.

## Requirements

- Python 3.x

The following libraries are required to run this script: (can be installed via `requirements.txt`)

- `requests`
- `requests-html`
- `beautifulsoup4`

## Installation

```
git clone https://github.com/ryanwaugh/linkedin-search
cd linkedin-search
python -m venv .
./Scripts/activate
pip install -r requirements.txt
```

## Usage

```
$ python linkedin_search.py -h
usage: linkedin_search.py [-h] [-t TITLE] [-l LOCATION] [-d]

Search for jobs on LinkedIn

options:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        job title of interest
  -l LOCATION, --location LOCATION
                        location of interest
```

To run the program, open a terminal and enter the following:

    $ python linkedin_search.py -t "job title" -l "location"

Be sure to wrap the title and location in quotation marks if they have spaces in their names. The program will display the job listing results in the terminal window.

## Note:

LinkedIn's default search response makes it such that this tool will always return one "full page" of 25 listings. Therefore, further attempts to allow for additional listings to be displayed from a looping prompt are scrapped.

I hope you will enjoy receiving exactly 25 job results, no matter the query.
