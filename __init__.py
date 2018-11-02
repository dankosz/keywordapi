import urllib.request, urllib.error, urllib.parse
import json
import MySQLdb
import os

from xploreapi import XPLORE
from TosDao import TOSDAO

## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

#xploreapi
xplore = XPLORE(config['apikey'])

#db
tosDao = TOSDAO(config)

publications = tosDao.getArticlesWithoutKeywords()

count = 0

try:
    for publication in publications:
        print("Fetching keywords for publication: ", publication.title)
        xplore.articleTitle(publication.title)
        articleData = json.load(urllib.request.urlopen(xplore.callAPI(False)))
        if bool(articleData['articles'][0]['index_terms']):
            keywords = articleData['articles'][0]['index_terms']['ieee_terms']['terms']
            for key in keywords:
                print(key)
            tosDao.insertKeyword(keywords, publication.id)
            count = count+1
except urllib.error.HTTPError as e:
    if hasattr(e,'code'):
        print(e.code)
        if (e.code = 403)
            print("API call limit has reached. Try running it with an other API key or ")
    if hasattr(e,'reason'):
        print(e.reason)
    print("Inserted ", int(count)," records from publications")