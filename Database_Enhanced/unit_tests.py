import unittest # Loads the testing system (framework)
from CRUD_Python_Module import AnimalShelter

#This class contains the tests.
class UnitTestingAnimalShelter(unittest.TestCase):

    # This restarts each independent check so that it is refreshed; no left over variables, connections, etc. so it 
    # will not ruin the next test that starts. It is just makes it empty/clean each time it starts.
    # In addition, avoids redundancy, otherwise we have to write this insde every test: shelter= AnimalShelter().
    def setUp(self):
        self.shelter = AnimalShelter()

    # This tests one animal record, and the categories chosen represent CRUD module expectation.
    def test_creation_rec_(self):
        rec = { "animal_id": 3453, "name": "Floppy", "breed": "Husky", "age": 8 }

        # calls the create() method and then stores the result.
        # will return True if the record is valid.
        result = self.shelter.create(rec)
        self.assertTrue(result)   #checks if it is True; assertion was chosen since create() can return a boolean.

        # Despite how there was tearDown() that's part of unittests framework, delete was chosen since it uses CRUD and avoids extra methods.
        # and reduces repitition (took tearDown() out and left in delete.)
        # Here will clean up the record so it does not sit at the database. 
        self.shelter.delete({"animal_id": 3453})


    # Tests is to check that read() can successfully get a record from the database.
    def test_read_rec(self):
        rec = { "animal_id": 2323, "name": "Stew", "breed": "Chihuahua", "age": 16 }
        self.shelter.create(rec) # needs to read existing in database (needs something to search for).

        # Using read() will look for the record we just inserted to be tested.
        # I used a simple query that uses unqiue animal_id.
        result = self.shelter.read({"animal_id": 2323})
        self.assertTrue(len(result) > 0)   # returns list of matching documents, used assertTrue to make sure the list is not empty.

        #clean out test record so it doesn't stay in database.
        self.shelter.delete({"animal_id": 2323})


    # Tests to is if it changes the record in the database.
    def test_update_rec(self):
        # Input a record so that we can update the categories.
        # I will do an example by updating the age of the dog. 
        rec = { "animal_id": 7286, "name": "Balto", "breed": "Shepherd", "age" : 2 }
        self.shelter.create(rec) # need record to read.

        # Dictionary represents the updated category (change from age 2 to 1).
        updated_categories = {"age": 1}

        # calls update() with the unique identifier and should return True IF the update succeds. 
        result = self.shelter.update({"animal_id": 7286}, updated_categories)
        self.assertTrue(result)

        # confirming that update had actually happened. 
        updated_record = self.shelter.read({"animal_id": 7286})

        # checking in age field that it actually updated to 1 years old.
        # Used assertEqual() since I am checking a certain value.
        self.assertEqual(updated_record[0]["age"], 1)

        # clean up for database
        self.shelter.delete({"animal_id": 7286})

    # Tests to make sure that the record is removed from the database.
    def test_delete_rec(self):
        # need to input a record so that delete() can have something to remove.
        rec = { "animal_id": 9989, "name": "Pebbles", "breed": "Saint Bernard", "age": 7 }
        self.shelter.create(rec)

        # unique identifier is being used by call delete(), if it returns True the deletion succeeded.
        result = self.shelter.delete({"animal_id": 9989})
        self.assertTrue(result)

        # checks if the deletion happened.
        deleted_check = self.shelter.read({"animal_id": 9989})

        # after recorded has been deleted, the read() should return an empty list.
        # used assertEqual() for this to make sure the list length is 0.
        self.assertEqual(len(deleted_check), 0)