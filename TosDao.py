import json
import MySQLdb
import pubinfMapper

class TosDao:
    
    def __init__(self, configfile):
        ## Load configuration
        con_file = open(configfile)
        config = json.load(con_file)
        con_file.close()
        #db connection
        self.conn = MySQLdb.connect(config['mysql_host'], 
        config['mysql_user'], config['mysql_password'], 
        config['mysql_database'])
        
    def getArticles(self):
        publications = []
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor);
        cursor.execute("SELECT * FROM pubinf")
        result_set = cursor.fetchall();
        for row in result_set:
            publication = pubinfMapper.mapRow(row)
            print(publication.title)
            publications.append(publication)
        return publications
        
        