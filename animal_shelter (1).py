from pymongo import MongoClient

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host='nv-desktop-services.apporto.com', port=31580):
        """ Initialize the MongoClient with authentication """
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}")
            self.database = self.client['AAC']  # Use the AAC database
            self.collection = self.database['animals']  # Use the animals collection
        except Exception as e:
            raise Exception(f"Failed to connect to database: {e}")

    def create(self, data):
        """ Create a new document in the collection """
        if isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise TypeError("Data should be a dictionary.")

    def read(self, query):
        """ Read documents based on a query """
        if isinstance(query, dict):
            try:
                result = self.collection.find(query)
                return list(result)  # Return results as a list
            except Exception as e:
                print(f"An error occurred: {e}")
                return []
        else:
            raise TypeError("Query should be a dictionary.")
