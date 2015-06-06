import scraperwiki
import sys, requests, bs4

# import os, errno, optparse

root = 'http://spectrum.ieee.org'
baseUrl = root + '/blog/riskfactor/page/'              # starting url
linkSelector = 'article > a'

sitemap = root + '/sitemap.xml'
sitemapFilter = 'riskfactor'

links = []

def parseSitemap():
    res = requests.get(sitemap)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    potentialLinks = soup.select('loc')

    for link in potentialLinks:
        if sitemapFilter in link.string:
            links.append(link.string)
            print link.string

    saveLinks()
    
def saveLinks():
    # Save the links to SQLite database
    uniques = set(links)
    for item in uniques:
        scraperwiki.sqlite.save(unique_keys=['url'], data={"url": item})
    linksFile.close()

    print 'Done.'
    
parseSitemap()

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful


# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
