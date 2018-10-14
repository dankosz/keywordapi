import urllib.request, urllib.error, urllib.parse
import json
import MySQLdb
import os

from xploreapi import XPLORE





## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

#xploreapy
xplore = XPLORE(config['apikey'])

#db connection
db = MySQLdb.connect(config['mysql_host'], config['mysql_user'], config['mysql_password'], config['mysql_database'])

cursor = db.cursor();

cursor.execute("SELECT title FROM pubinf")

titles = cursor.fetchall()

for title in titles:
    xplore.articleTitle(title[0])
    articleData = json.load(urllib.request.urlopen(xplore.callAPI(False)))
    if bool(articleData['articles'][0]['index_terms']):
        for key in articleData['articles'][0]['index_terms']['ieee_terms']['terms']:
                print(key)
            

#for x in content['articles'][0]['index_terms']['ieee_terms']['terms']:
  #print(x)
