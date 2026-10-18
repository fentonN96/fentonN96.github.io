from CRUD_Python_Module import AnimalShelter

shelter = AnimalShelter() # will connect to database using enhanced CRUD module. 

#Testing ID for database, since I do not have the actual ACC collection data.
test_ID = 123789

print("\nDatabase Enhancement Tests")

# We will be doing seven tests: Create, Projection, Negative age,
#    partial update, Empty update query, Empty delete query, Clean up. 
#-----------------------------------------------------------------------------

# Test 1: Chekcing when creating valid data
print("\nTest One: Create a valid animal")
test_animal = {
    "animal_id": test_ID, 
    "name": "Test Animal",
    "breed": "Test Breed",
    "age": 3
    }
result = shelter.create(test_animal)
print("Here are the results for create:", result)
#--------------------------------------------------------

# Test 2: Read using projection 
print("\nTest Two: Using Projection with Read animal")
result = shelter.read(
    {"animal_id" : test_ID},
    {
        "_id": 0,
        "animal_id": 1,
        "name": 1, 
        "breed": 1, 
        "age": 1
    }
)
print("Results using projection:", result)
#---------------------------------------------------------

# Test 3: Invalid data such as using negative
print("\nTest Three: Do not allow negative age")
invalid_animal = {
    "animal_id": 383894,
    "name": "Invalid Animal",
    "breed": "Test Breed",
    "age": -12
}
result = shelter.create(invalid_animal)
print("Invalid create result:", result)
#----------------------------------------------------------

# Test 4: be able to update animal's age
print("\nTest Four: Update the animal's age")
result = shelter.update(
    {"animal_id": test_ID},
    {"age": 2}
)
print("Animal's age updated:", result)
#----------------------------------------------------------

# Test 5: When there is an empty update
print("\nTest Five: Do not allow an empty update query")
result = shelter.update(
    {},
    {"age": 3}
)
print("Empty query update result:", result)
#----------------------------------------------------------

# Test 6: when there is an empty delete
print("\nTest Six: Do not allow an empty delete query")
result = shelter.delete({})
print("Empty query delete result:", result)
#----------------------------------------------------------

# Test 7: Being able to delete a record
print("\nTest Seven: Be able to delete a record")
result = shelter.delete(
    {"animal_id": test_ID}
)
print("Documents deleted:", result)
#----------------------------------------------------------

print("\nTesting Completed")