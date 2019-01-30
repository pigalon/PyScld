from arango_orm import Database
from arango import ArangoClient

class DatabaseAdb():
    
    def __init__(self, db_name):
        self.db_name = db_name

    def initDB(self):
        client = ArangoClient(protocol='http', host='localhost', port=8529)
        test_db = client.db(self.db_name, username='root', password='')
        return Database(test_db)
        

   
        