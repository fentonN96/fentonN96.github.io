# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'REDACTED' 
        PASS = 'REDACTED' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    # Method adds new documents to the animal collection, and data willl be dictionary that has key/value pairs.
    def create(self, data):
        if not data: 
            print("Creating document has failed; no data was provided.") #if data is missing
            return False # nothing will be inserted if it returned false.
        
        try: 
            # insert_one would add one document to MongoDB
            # This is done by going into the acca database, find 'animals' collection, and save it inside self.collection.
            self.collection.insert_one(data)
            return True # line will run if the inserted worked. 
        
        # if anything goes wrong, it will print the error to understand what happened.
        except Exception as error:
            print("There was an Error when inserting document:", error)
            return False # insert failed

    # Create method to implement the R in CRUD.
    # In the animal collection the methods search through its documents.
     # query argument should be a dictionary describing what to look for. 
    def read(self, query):
        
        # note: find() returns a cursor, kinda points where the results are located at.
        # Here the process converts the cursor into a list in order to see all the documents at once. 
        try:
            results = list(self.collection.find(query)) # when the query is running; results are converted to a list.
            return results # the list of documents is returned.
                           
        # if something goes worng, it will print the error and return the list empty.
        except Exception as error:
            print("When reading the documents there is an error:", error)
            return [] # failed to read and so it returns an empty list. 
      
    # Update method to input the U in CRUD.
    # Looks for documents in MongoDB collection, matches information, and
    # then updates them. 
    def update(self, query, new_values): #query tells MongoDB what documents to look for. 
                                        #new_values tell MongoDB what fields to change. 
        try: 
            return self.collection.update_many( # updates all the documents that match query
                query, {"$set": new_values}).modified_count # query filters
                                                            # $set tells MongoDB what field needs to be updated
                                                            # gives results back on whats been updated
        
        except Exception as error: #caught update errors
            print ("An error happened when updating documents(s):", error) # notify the user what type of error.
            return 0 # updated had failed and return to 0.
        
    # Delete method for D in CRUD
    # removes documents that match the query
    def delete(self, query): # query for this means which documents is removed
        try: 
            #delete_may removes all that matches instructions (query).
            # query then filters to find those to remove.
            return self.collection.delete_many(query).deleted_count # deleted_count gives back the results on what were deleted.
        
        except Exception as error: #catches deleted-related errors.
            print("An error happened deleting document(s):", error) # notify the user of type of error.
            return 0 # not able to delete and return to 0. 
            
     