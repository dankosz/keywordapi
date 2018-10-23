import json
import MySQLdb
import sys

from mapper import MAPPER

class TOSDAO:
    
    def __init__(self, config):
        #db connection
        self.conn = MySQLdb.connect(config['mysql_host'], 
        config['mysql_user'], config['mysql_password'], 
        config['mysql_database'])
        self.conn.autocommit = True
        #dictcursor
        self.dictCursor = self.conn.cursor(MySQLdb.cursors.DictCursor);
        
    def getArticles(self):
        publications = []
        self.dictCursor.execute("SELECT * FROM pubinf")
        result_set = self.dictCursor.fetchall()
        for row in result_set:
            publication = MAPPER.mapRow(row)
            publications.append(publication)
        return publications
        
    def insertKeyword(self, keywords, pubinfId):
        try:
            for keyword in keywords:
                #check if keyword already exists
                self.dictCursor.execute("SELECT * FROM keywords WHERE keyword = %(keyword)s", {'keyword': keyword})
                result_set = self.dictCursor.fetchall()
                print(result_set)
                if bool(result_set):
                    print("keyword %s already exists in db", (keyword))
                    existingKeyword = MAPPER.mapRow(result_set[0])
                    keywordCount = existingKeyword.keywordcount + 1 
                    keywordId = existingKeyword.id
                    #if yes, increment the keywordCount
                    print("Updating keyword with keywordcount: %s" (int(keywordCount)))
                    self.dictCursor.execute("UPDATE keywords SET keywordcount = %s WHERE id = %s", (int(keywordCount), int(keywordId)))
                else:
                    #if not, insert it
                    print("inserting keyword into keywords table: %s", (keyword))
                    self.dictCursor.execute("INSERT INTO keywords (keyword, keywordcount) VALUES(%s, %s)", (keyword, int(0)))
                    #insert into the connector table
                    insertedKeywordId = self.conn.insert_id()
                    print("inserting into keywordpubs keywordId: %s, pubinfId: %s", (int(insertedKeywordId), int(pubinfId)))
                    self.dictCursor.execute("INSERT INTO keywordpubs (keywordid, id) VALUES(%s, %s)", (int(insertedKeywordId), int(pubinfId)))
                    #refresh view (nodes)
                    print("inserting into nodes insertedKeywordId: %s, type: keyword, label: %s, title: %s", (int(insertedKeywordId), keyword, keyword))
                    self.dictCursor.execute("INSERT INTO nodes (rowid, type, label, title) VALUES(%s, %s, %s, %s)", (int(insertedKeywordId), "keyword", keyword, keyword))
                    keyword_node_id = self.conn.insert_id()
                    #refresh edges
                    self.dictCursor.execute("SELECT * FROM nodes WHERE rowid = %s AND type = %s", (pubinfId, "publ"))
                    pub_res = self.dictCursor.fetchall()
                    print(pub_res)
                    publication_node = MAPPER.mapRow(pub_res[0])
                    print("inserting into edges start: %s, end: %s, type: desc", (int(publication_node.id), int(keyword_node_id)))
                    self.dictCursor.execute("INSERT INTO edges (start, end, type) VALUES(%s, %s, %s)", (int(publication_node.id), int(keyword_node_id), "desc"))
        except:
            print("Unexpected error, rolling back:", sys.exc_info()[0])
            self.conn.rollback()
            raise
        
        
        
        
        
        
        
        
        
        
        
        
            
            