import urllib2
import json

from xploreapi import XPLORE


xplore = XPLORE("sw4kycygk4ac5vf5ces72mp8")




#for each article title:
    #xplore.articleTitle(title)
    #articleData = json.load(urllib2.urlopen(xplore.callAPI(True)))
    #if bool(content['articles'][0]['index_terms'])
        #index terms -> type -> []
        #for key in content['articles'][0]['index_terms']:
            #save key and corresponding list of keywords to db

xplore.articleNumber("1")


content = json.load(urllib2.urlopen(xplore.callAPI(False)))

#for x in content['articles'][0]['index_terms']['ieee_terms']['terms']:
  #print(x)
for key in content['articles'][0]['index_terms']:
    print(key)

print(content['articles'][0]['index_terms']['ieee_terms']['terms'])