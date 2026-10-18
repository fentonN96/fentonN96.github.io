# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

# Load from the .env files (contains the environment variables).
# Note: dotenv lets Python read values and os give access. 
# Removes hardcoded credentials and is now secure. 
from dotenv import load_dotenv
import os 

import logging #brings a python built-in logging system

# Configuring Logging
logging.basicConfig(
    # All logs will be written in this file (gives permanent record of what happends in CRUD module).
    # how real life programs track problems.
    filename="animal_shelter.log", 

    # This will tell Python what types of messages to save.
    # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. We have INFO: normal operation messages.
    level=logging.INFO, # means save all from INFO and above (includes: INFO, WARNING, ERROR, CRITICAL). DO not want too much noise.
    
    # Controls how each log entry looks: 
    #    timestamp (when event happened)
    #    Type of level message (ERROR, INFO, etc.)
    #    Text logged
    format="%(asctime)s - %(levelname)s -%(message)s"
)

# Added logging
#______________________________________________________________________________________________________________________________________________

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Environment variables wil be loaded from the .env file. 
        # Has secure coding practices by removing hardcoded credentials. 

        # .env file is now read.
        load_dotenv(dotenv_path=".env") 

        # Get MongoDB connection settings from the environment variables. 
        # Will be using os.getenv() to access environment variables (store sensitive info with system-wide key-value pairs).
        USER = os.getenv("DB_USER")
        PASS = os.getenv("DB_PASS")
        HOST = os.getenv("DB_HOST")
        PORT = int(os.getenv("DB_PORT"))
        DB = os.getenv("DB_NAME")
        COL = os.getenv("DB_COLLECTION")

        # 
        # Initialize Connection 
        # Change hardcoded connection (change from integers to strings: environment variable works). 
        # Needed to adjust to avoid mismatch and meet industry standard formatting. 
        # Note: MongoDB connection strings should always use text to be safe. 
        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}") 
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # credentials corrected.
    #_______________________________________________________________________________________________________________________________________________


    # Add in helper method so that it checks the before before sending it to the database.
    # Checks Existing and makes sense. This will be called in created() later. 
    def data_check (self, data):
        # These categories are required be in every animal document (otherwise if missing, broken data).
        animal_ReqCategories = ["animal_id", "name", "breed", "age"]

        # Checks if each categories exists in the data dictionary. 
        for categories in animal_ReqCategories: 
            # If not, program stops (raise ValueError) and then tells what is missing. 
            # Prevents bad data from entering database. 
            if categories not in data: 
                raise ValueError(f"A category is missing: {categories}")

        # Checks that animal_id is the correct type which needs to be a number; integer)
        # Note: isinstance will check the value's type
        if not isinstance(data["animal_id"], int):
            raise TypeError("animal_id must be an integer")

        # if everything is correct
        return True 
    
    # Inputted validation (Helper Method).
    #_____________________________________________________________________________________________________________________________________________


    # Create a method to return the next available record number for use in the create method
    # Complete this create method to implement the C in CRUD. 
    # Method adds new documents to the animal collection, and data willl be dictionary that has key/value pairs.
    def create(self, data):

        # Now performing validation checks
        # Checks if data is empty.
        if not data: 
            print("Creating has failed. No data inserted.")
            return False

        try: 
            # Here we inputted our helper function so we can run a validation.
            # Inputting validation check. 
            self.data_check(data)
            # Return it true if it meets the validation check.
            # This will put the document into the collection in the database.
            self.collection.insert_one(data)
            logging.info("Document created successfully.") #logged.
            return True # creation was successful, return to user.
        

        # Instead of just one error checks, we will expand to three.
        # This is print is for the user to read message while the error object is in detail is for the developer to read what's wrong.

        # Is activated when missing categories are founded by the helper method.
        # Raises ValueError if category is missing; gets a specific common problem and clear to understand.
        except ValueError as error: 
            print("Validation error:", error)             # User message: "Validation error".
                                                          # Developer message: "A category is missing: name".
            logging.error("Validation error: %s", error)  # Error is logged in file.
            return False #stops operations

        # Is activated when there is a wrong type
        # if its not a number; helps get a specific common problem and clear to understand.
        except TypeError as error:
            print("Type error:", error) # User message: "Type error".
                                        # Developer message: "animal_id must be an integer".
            logging.error("Type error: %s", error)
            return False

        # Is activated when there is an unexpected error (Huge safety net to catch all)
        # Examples: MongoDB connection problems, insert/update fails, network issues, typos, other unexpected problems
        except Exception as error:
            print("Unexpected error:", error) # User message: "Unexpected Error".
                                              # Developer message: "connection issue", "Failed to update", "Query is Invalid", etc.
            logging.exception("Unexpected error: %s", error)  # logged but with exception that includeds traceback.                              
            return False

    # Added missing Validation and safety checks (from helper method).
    # Added in more improved error handling.
    # Added in logging 
    # Improved modularity (helper method (data_check), environment variable loading, and logging setup)
    #__________________________________________________________________________________________________________________________________________


    # Read method to implement the R in CRUD.
    # In the animal collection the methods search through its documents.
     # query argument should be a dictionary describing what to look for. 
    def read(self, query):
        
        # note: find() returns a cursor, kinda points where the results are located at.
        # Here the process converts the cursor into a list in order to see all the documents at once. 
        try:
            results = list(self.collection.find(query)) # when the query is running; results are converted to a list.
            logging.info("Reading operation has been completed.") # confirm it ran, track how often read is used, exact timestamps.
            return results # the list of documents is returned.
                           
        # if something goes worng, it will print the error and return the list empty.
        except Exception as error:
            print("When reading the documents there is an error:", error)
            logging.error("Read error: %s", error) #logged for issues.
            return [] # failed to read and so it returns an empty list. 

    # Added logging   
    # Improved modularity (helper method (data_check), environment variable loading, and logging setup)
    #__________________________________________________________________________________________________________________________________________


    # Update method to input the U in CRUD.
    # Looks for documents in MongoDB collection, matches information, and
    # then updates them. 
    def update(self, query, new_values): #query tells MongoDB what documents to look for. 
                                        #new_values tell MongoDB what fields to change. 
        
        # Now performing validation checks
        # Checking query if its empty.
        # Prevents from updating ALL the documents by accident, especially if query is in {}.
        if not query:
            print("Update has failed; no query was provided.")
            return 0

        # Checking if new_values is empty.
        # Avoids pointless updates. 
        if not new_values:
            print("Update has failed; no new values were provided.")
            return 0
       
        try:  
            # Will not do a full record update like create(), update() only changes some fields.
            # Partial Validation. This prevents bad updates.
            if "animal_id" in new_values and not isinstance(new_values["animal_id"], int):
                raise TypeError("animal_id must be an integer")

            if "age" in new_values and not isinstance(new_values["age"], int):
                raise TypeError("age must be an integer")

            # Perform the update to the database. 
            # Note: update_many(query, {"$set": new_values}) if matched, it will update all of those matched documents. 
            #       $set will have certain categories to changed told by MongoDB. 
            result = self.collection.update_many(query, {"$set": new_values})
            logging.info("Updated %s documents.", result.modified_count)
            return result.modified_count # returns how many documents were updated.
        
        # Is activated when there is an unexpected error (Huge safety net to catch all)
        # Examples: MongoDB connection problems, insert/update fails, network issues, typos, other unexpected problems
        except Exception as error:
            print("Unexpected error:", error) # User message: "Unexpected Error".
                                              # Developer message: "connection issue", "Failed to update", "Query is Invalid", etc.
            logging.exception("Unexpected error: %s", error) #logged but with exception.
            return False

    # Add missing Validation and safety checks (helper methods).
    # Added in more improved error handling.
    # Added logging.
     # Improved modularity (helper method (data_check), environment variable loading, and logging setup)
    #________________________________________________________________________________________________________________________________________
        
    # Delete method for D in CRUD
    # removes documents that match the query
    def delete(self, query): # query for this means which documents is removed
        try: 
            result = self.collection.delete_many(query)
            # query then filters to find those to remove.
            logging.info("Deleted %s documents.", result.deleted_count) # logged
            return result.deleted_count #document deleted.
        
        except Exception as error: #catches deleted-related errors.
            print("An error happened deleting document(s):", error) # notify the user of type of error.
            logging.exception("Delete error: %s", error) # logged but with exception.
            return 0 # not able to delete and return to 0. 

    # Added logging.
    # Improved modularity (helper method (data_check), environment variable loading, and logging setup)
    #_______________________________________________________________________________________________________________________________________

# Test for connection that everything connects for loading enivornment variable.
if __name__ == "__main__":
    shelter = AnimalShelter()
    print("Connection worked:", shelter.client is not None)    
     