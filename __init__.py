import urllib.request, urllib.error, urllib.parse
import json
import MySQLdb
import os

from xploreapi import XPLORE
from TosDao import TOSDAO

#xploreapi
xplore = XPLORE(config['apikey'])

#db
tosDao = TOSDAO("config.json")

publications = TOSDAO.getArticles()


for publication in publications:
    print("Fetching keywords for publication: " %(publication.title))
    xplore.articleTitle(publication.title)
    articleData = json.load(urllib.request.urlopen(xplore.callAPI(False)))
    if bool(articleData['articles'][0]['index_terms']):
        for key in articleData['articles'][0]['index_terms']['ieee_terms']['terms']:
                print(key)