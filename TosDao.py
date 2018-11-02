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
    
    def getArticlesWithoutKeywords(self):
        publications = []
        self.dictCursor.execute("SELECT p.title, kp.keywordid FROM pubinf p LEFT JOIN keywordpubs kp ON p.id=kp.id WHERE kp.id IS NULL")
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
                keywordId = 0;
                keyword_node_id = 0;
                print(result_set)
                if bool(result_set):
                    print("keyword already exists in db: ", keyword)
                    existingKeyword = MAPPER.mapRow(result_set[0])
                    keywordCount = existingKeyword.keywordcount + 1 
                    keywordId = existingKeyword.id
                    #if yes, increment the keywordCount
                    print("Updating keyword with keywordcount: ", int(keywordCount))
                    self.dictCursor.execute("UPDATE keywords SET keywordcount = %s WHERE id = %s", (int(keywordCount), int(keywordId)))
                else:
                    #if not, insert it
                    print("inserting keyword into keywords table: ", keyword)
                    self.dictCursor.execute("INSERT INTO keywords (keyword, keywordcount) VALUES(%s, %s)", (keyword, int(0)))
                    keywordId = self.conn.insert_id()
                #check if node already exists
                self.dictCursor.execute("SELECT * FROM nodes WHERE rowid = %s AND type = %s", (int(keywordId), "keyword"))
                node_set= self.dictCursor.fetchall()
                if bool(node_set)
                    print("keyword node already exists in db: ", keyword)
                    existingKeywordNode = MAPPER.mapRow(node_set[0])
                    keyword_node_id = existingKeywordNode.rowid
                else:
                    #insert keywordnode
                    print("inserting into nodes insertedKeywordId:", int(insertedKeywordId), ", type: keyword, label: ", keyword[0:31], ", title: ", keyword)
                    self.dictCursor.execute("INSERT INTO nodes (rowid, type, label, title) VALUES(%s, %s, %s, %s)", (int(insertedKeywordId), "keyword", keyword[0:31], keyword))
                    keyword_node_id = self.conn.insert_id()
                #insert into the connector table
                print("inserting into keywordpubs keywordId:", int(keywordId), ", pubinfId: ", int(pubinfId))
                self.dictCursor.execute("INSERT INTO keywordpubs (keywordid, id) VALUES(%s, %s)", (int(keywordId), int(pubinfId)))
                #refresh edges
                self.dictCursor.execute("SELECT * FROM nodes WHERE rowid = %s AND type = %s", (pubinfId, "publ"))
                pub_res = self.dictCursor.fetchall()
                print(pub_res)
                publication_node = MAPPER.mapRow(pub_res[0])
                print("inserting into edges start: ", int(publication_node.id), ", end: ", int(keyword_node_id), ", type: desc")
                self.dictCursor.execute("INSERT INTO edges (start, end, type) VALUES(%s, %s, %s)", (int(publication_node.id), int(keyword_node_id), "desc"))
        except:
            print("Unexpected error, rolling back:", sys.exc_info()[0])
            self.conn.rollback()
            raise
        self.conn.commit()
        
        
        
        
        
        
        
        
        
        
        
        
            
            