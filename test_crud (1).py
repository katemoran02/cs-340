from crud import CRUD

# Instantiate the CRUD class
crud = CRUD(db_name="austin_animal_center", collection_name="outcomes", user="aacuser", password="YourSecurePassword")

# Test Create
data = {"name": "Rex", "age": 3, "breed": "German Shepherd"}
print("Create:", crud.create(data))

# Test Read
query = {"breed": "German Shepherd"}
print("Read:", crud.read(query))

# Test Update
update_data = {"age": 4}
print("Update:", crud.update({"name": "Rex"}, update_data))

# Test Delete
print("Delete:", crud.delete({"name": "Rex"}))
