from pymongo import MongoClient

class CRUD:
    def __init__(self, db_name, collection_name, user, password):
        self.client = MongoClient('mongodb://localhost:22804/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.db.authenticate(user, password)
    
    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            return False
    
    def read(self, query):
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Error reading data: {e}")
            return []
    
    def update(self, query, new_data):
        try:
            result = self.collection.update_many(query, {'$set': new_data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating data: {e}")
            return 0
    
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting data: {e}")
            return 0
