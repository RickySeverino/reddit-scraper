#!/usr/bin/env python

import sys
import urllib.request
import simplejson as json
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
    print("\nUsage: rscrape.py subreddit")
    sys.exit()
elif len(sys.argv) == 2:
    subreddit = sys.argv[1]
    
url = "https://old.reddit.com/r/" + subreddit + "/new/"

#download the URL and extract the content to the variable html
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(request).read()

#pass the html to Beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

main_table = soup.find("div", attrs={'id':'siteTable'})

links = main_table.find_all("a", class_ = "title")

extracted_records = []

for link in links:

    title = link.text
    url = link['href']

    if not url.startswith('http'):
        url = "https://old.reddit.com" + url

    print("\n%s : %s"%(title, url))
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------")

    record = {
            'title':title,
            'url':url
            }

    extracted_records.append(record)

outfile = subreddit + ".json"

with open(outfile, 'w') as outfile:
    json.dump(extracted_records, outfile, indent=4)
