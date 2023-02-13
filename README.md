# LinkedIn Job Search

A simple program allowing you to search LinkedIn for job opportunities based on job title and location. It uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to scrape job listings from LinkedIn's job search page.

## Requirements

- Python 3.x

The following libraries are required to run this script:

- Requests library (can be installed using `pip install requests`)
- Requests-html library (can be installed using `pip install requests-html`)
- BeautifulSoup library (can be installed using `pip install beautilfulsoup4`)

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
  -d, --debug           Enable raw parser output to terminal
```

To run the program, open a terminal and navigate to the directory where the `linkedin_search.py` file has been `git clone`'d to. Then, run the following command:

    $ python linkedin_search.py -t "job title" -l "location"

Be sure to wrap the title and location in quotation marks if they have spaces in their names. The program will display the job listing results in the terminal window (currently broken by website change, use `--debug` to see the raw output).
