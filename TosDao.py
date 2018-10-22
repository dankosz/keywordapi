import json
import MySQLdb

from mapper import MAPPER

class TOSDAO:
    
    def __init__(self, config):
        #db connection
        self.conn = MySQLdb.connect(config['mysql_host'], 
        config['mysql_user'], config['mysql_password'], 
        config['mysql_database'])
        #dictcursor
        self.dictCursor = self.conn.cursor(MySQLdb.cursors.DictCursor);
        
    def getArticles(self):
        publications = []
        self.dictCursor.execute("SELECT * FROM pubinf")
        result_set = self.dictCursor.fetchall()
        for row in result_set:
            publication = MAPPER.mapRow(row)
            print(publication.title)
            publications.append(publication)
        return publications
        
    def insertKeyword(self, keywords):
        for keyword in keywords:
            #check if keyword already exists
            self.dictCursor.execute("SELECT * FROM keywords WHERE keyword = %s", (keyword))
            result_set = self.dictCursor.fetchall()
            if bool(result_set[0]):
                existingKeyword = MAPPER.mapRow(result_set[0])
                keywordCount = existingKeyword.keywordcount + 1 
                keywordId = existingKeyword.id
                #if yes, increment the keywordCount
                self.dictCursor.execute("UPDATE keywords SET keywordcount = %s WHERE id = %s", (int(keywordCount), int(keywordId)))
            else:
                #if not, insert it
                self.dictCursor.execute("INSERT INTO keywords (keyword, keywordcount) VALUES(%s, %s)", (keyword, int(0)))
        self.conn.rollback()
            
            