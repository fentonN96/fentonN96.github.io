# Computer Science ePortfolio
**By Natalie Fenton**

Computer Science | Software Engineering Concentration

---

## Professional Self-Assessment
With the Computer Science program now completed, I have now looked back and noticed how much I have grown my skills in problem-solving abilities along with a change of mind set to achieve progressing in this field. In the beginning courses, I had been so focused on making sure the code worked and that the results were correct. During the middle classes of my program, I started being taught theories and standards in software development, which opened my mind to the fact that it was more than just trying to get a program to run. This involved the code having an organized structure, keeping secured, organizing, and making it maintainable so that if another worker comes to review it; they can understand it too. Creating this ePortfolio has allowed me to look back on my past classes to compare and contrast with the knowledge and experience I have now to make quality, standard decisions when going to work in my job field. 

[Read My Full Professional Self-Assessment](professional-self-assessment.md)

## Code Review
In this code review, I explain my skills by improving my original artifacts by adding security, error handling, and maintainability, and by improving scalability and overall quality for this capstone. I will also be going over my thought process on why the current functions cause problems and why I chose specific approaches to replace them to potentially solve it in enhancement terms. The review will look into my two past course projects: Python CRUD and C++ Course Planner. In addition, these enhancements are going to be in three categories which are software design and engineering, algorithms and data structures, and databases. The review establishes the starting point for the three enhanced artifacts presented in this ePortfolio.

[Watch Video Capstone Code Review](https://youtu.be/_UZfxi53GT8)

## Software Design & Engineering 
**Artifact:** Python CRUD Module

**Course:** CS 340: Client/Server Development 

Python CRUD Module project in CS 340: Client/Server Development has shown how an application can perform CRUD operations while using a MongoDB database. I have chosen this artifact since I have gained more experience in backend development and wanted to apply the skills I have learned while also researching areas that were new to me. Going back to the original artifact and evaluating, I noticed a couple of areas needing an upgrade: database configuration, validation, error handling, testing, and more other improvements. My Software Design and Engineering enhancement was mainly focused on improving the quality areas and being able to show the software engineering practices I have developed throughout the Computer Science program.

### Original Artifact
The original artifact had the basic CRUD operations needed to create, read, update, and delete animal records within a MongoDB database. Although the program was functional for the original CS 340 assignment, revisiting the code showed areas that could be improved in its structure, security, validation, logging, and testing. One huge issue was that the database credentials were hardcoded directly into the original source code. Reviewing these limitations gave me the starting point for the Software Design and Engineering enhancement.

**Security Note:"" Credentials were redacted due to public portfolio publication exposure. Despite the sensitive credential values, the files still represent the original implementations.

[View Original CRUD Source Code](CRUD_Python_Module.pyw) 

### Enhanced Artifact 
The enhanced artifact's CRUD module had been moved from a Codio environment to an authenticated MongoDB installation on my computer. I replaced the hardcoded connection information with environment variables and had to troubleshoot mismatched .env names and the working directory used by Visual Studio Code. I also added the data_check() method, structured logging, clearer error handling, and unit tests for all four CRUD operations. These changes made the module easier to troubleshoot, safer to configure, and more reliable when working with animal records.

[View Enhanced CRUD Source Code](CRUD_Python_Module.py)

[View Unit Tests](unit_tests.py)

**Key Enhancements:**

- Environment-based database configuration

- MongoDB authentication

- Record validation through data_check()

- Structured logging

- Improved exception handling

- CRUD unit testing

### Skills Demonstrated
One of the biggest challenges I had with this enhancement was getting MongoDB to connect correctly after moving away from the Codio environment. When I first tried using the .env file, Python kept loading None for every variable, and my connection string came out as mongodb://None:None@None:None. At first, I thought I had only named the variables incorrectly, so I changed them to match what my CRUD module expected. However, it still returned None, and I eventually found that Visual Studio Code was running my test from a different working directory and couldn't find my .env file. Fixing these problems helped me better understand how the Python module, environment configuration, and MongoDB connection all have to work together.

**Technical Skills:**

- Python and PyMongo
  
- MongoDB authentication
  
- Environment variables

- Input validation and error handling
  
- Logging
  
- CRUD unit testing

### Enhancement Narrative
[Read the Software Design & Engineering Enhancement Narrative](software-engineering-narrative.md)

## Algorithms & Data Structures 
**Artifact:**: Course Planner

**Course:** CS 300: Data Structures and Algorithms 
The Course Planner project was made in CS 300 DSA: Analysis and Design to store course information and allow the user to view the course list or search for a specific course and its prerequisites. I chose this artifact because when I originally completed the course, I was still new to sorting and searching algorithms in C++. Going back to this project allowed me to look at the same program again with more experience and think more carefully about how the data structure and search algorithm work together.

### Original Artifact
The original Course Planner stored the course objects in a vector and then searched through the courses using a linear search. The program would check the courses one by one till it came across the user's request. When making this project, I was still trying to learn about different searching and sorting techniques in C++; so the linear search was easier for me to understand and implement. When I look back at it now, I can see how this approach works for a small amount of course data, but it would require more searching as additional courses were added and would make the program slower. The original version also used a raw pointer for the data structure and had limited input validation and error handling. These were areas I wanted to go back to because I now had a better understanding of algorithm efficiency, memory management, and how the program could handle incorrect user input.

[View Original Course Planner C++](Algorithms_Data_Structures_Original/ProjectTwo.cpp) 

### Enhanced Artifact
One of the main improvements I made during this course, I replaced the linear search with a binary search. The original linear search had a time complexity of O(n), while the binary search reduces the search time to O(log n). I also had to make sure the course data was sorted because binary search depends on the data being in order. For this part, I used a lambda comparator with the vector to organize the courses by course number.

[View Enhanced Course Planner C++](Algorithms_Data_Structures_Enhanced/ProjectTwoCapstone.cpp)

I also added input validation to check the course number before searching for it and included exception handling for cases where a course could not be found. Another change was replacing the raw pointer with unique_ptr and make_unique. This allowed the program to manage the memory automatically instead of relying on the manual new and delete approach used in the original version.

**Key Enhancements:**

- Replaced linear search O(n) with binary search O(log n)

- Used a sorted vector to support binary search

- Added a lambda comparator for sorting course numbers

- Added course-number input validation

- Added exception handling for unsuccessful searches

- Replaced a raw pointer with unique_ptr and make_unique

- Added additional comments to explain the algorithm and program structure

### Skills Demonstrated 
One of the new things I had to learn was that I could not just replace linear search with binary search; there was a format I needed to follow first. The course data needed to be sorted first, which helped me understand how the algorithm and data structure depend on each other. I also started thinking more about scalability. Even though the Course Planner only has a small number of courses right now, binary search would be more useful as the amount of data grows.

I also got more experience with memory management by replacing the raw pointer with unique_ptr and make_unique. Adding validation and exception handling made me think beyond whether the search simply worked and more about how the program should respond when something goes wrong. Overall, this enhancement helped me understand how several smaller design choices can work together to improve the program

**Technical Skills:**

- C++
  
- Vectors and data organization
  
- Algorithm complexity analysis
  
- Lambda expressions and sorting
  
- Input Validation
  
- Exception handling
  
- Smart pointers and memory management

### Enhancement Narrative 
[Read the Algorithms and Data Structure Enhancement Narrative](algorithms-narrative.md)

## Databases 

**Artifact:** Python CRUD Module

**Course:** CS 340: Client/Server Development 

The Database enhancement uses the same Python CRUD Module from CS 340: Client/Server Development that I previously used for my Software Design and Engineering enhancement. Instead of starting over with the original project, I continued working from the improved version so I could keep changes I had already made, such as environment-based configuration, logging, validation, and better error handling. For this category, I wanted to focus more specifically on how the application communicates with MongoDB and how the database operations could become safer, more efficient, and more reliable.

When I looked at the project from more of a database perspective, I noticed areas that I had not focused on during the Software Engineering enhancement. The application still needed better query validation, indexing, data-integrity protection, and safeguards around update and delete operations. I also wanted to improve how information was retrieved from MongoDB and how database-specific failures were handled. This gave me a way to continue improving the same artifact while showing a different set of skills related specifically to databases.

### Original Artifact 
The original Python CRUD Module showed the basic connection between a Python application and MongoDB. It allowed the application to create, read, update, and delete animal records, which gave me my first experience with backend database operations. When I went back to the project during the capstone, I noticed that the original version was mainly focused on getting the CRUD operations to function. It had hardcoded database credentials and did not have the validation, logging, query safeguards, or database protections that I later added. This original version gives me a starting point to show how much the project changed throughout the capstone.

Security Note: Credentials in the original artifact were redacted to prevent sensitive information from being exposed through the public ePortfolio. Other than the redacted credential values, the files represent the original implementation.

[View Original CRUD Source Code](CRUD_Python_Module.pyw) 

### Software Design & Engineering Enhancement 
I had already built a Python CRUD project for Software Design and Engineering, so using the same project for the Database enhancement had an impact on how I wanted the application to operate. I had to switch my mindset and focus mainly on the database side while still keeping the improvements I had already made, including environment variables and authentication, validation, logging, improved error handling, and unit testing. Instead of removing those improvements for Category Three, I kept them and used that enhanced version as my new starting point. This allowed me to focus specifically on the database layer without taking the application backward or repeating the same enhancement. It also made the process less confusing because I could continue building on the work I had already completed instead of making unnecessary changes between the Software Design and Engineering and Database versions.

[View Enhanced CRUD Source Code](CRUD_Python_Module.py)

### Final Database Enhancement
For the final Database enhancement, I focused more on what happens before information reaches MongoDB and how database operations could be made safer and more reliable. I added an index on animal_id to support more efficient lookups and created query_check() to validate MongoDB queries before they are used. I also added protections against empty update and delete queries because those operations could affect more records than intended.

[View Final Database Enhanced Source](Database_Enhanced/CRUD_Python_Module.py)

[View Database Enhancement Tests](Database_Enhanced/database_tests.py) 

Another challenge involved data validation. My original data_check() method expected a complete animal record, but an update may only need to change one field. I did not want someone to have to provide the entire animal record just to update something such as the age. Because of this, I kept the complete validation for create() and used partial validation in update() so that only the fields being changed are checked. I also added optional projection to read() so the application can request only the fields it needs, along with MongoDB-specific ConnectionFailure and OperationFailure handling.

**Key Enhancements:**

- Added an index on animal_id

- Added MongoDB query validation through query_check()

- Added stronger data-integrity checks

- Protected update and delete operations from empty queries

- Added separate validation for partial updates

- Added optional projection to read()

- Added MongoDB-specific ConnectionFailure handling

- Added MongoDB-specific OperationFailure handling

- Created database_tests.py using controlled temporary records

- Preserved secure environment-based database configuration from the Software Engineering enhancement

### Skills Demonstrated 
One of the most challenging things I learned from this enhancement was that database security is not only about protecting a username and password. I also had to think about protecting the information stored inside the database. For example, an empty query means something completely different depending on the CRUD operation. For example, an empty read might potentially return records, but an empty update or delete could unexpectedly change or remove many records. Realizing the difference made me cautious and had me put more thought into each database operation, so I am not blindly using the same validation everywhere.

I also had to make decisions without having access to my original AAC dataset; my old course for it provided Codio. I considered making the animal_id index unique, but I could not check that every existing animal_id was unique. Instead of making that guess, I had to just stick with the regular index. In addition, I created database_tests.py with temporary animal records so I could still test the database enhancement without having to depend on the missing original dataset. That experience helped me understand that testing does not always mean proving that an operation succeeds. Some of my successful tests were actually proving that unsafe or invalid operations were correctly rejected

**Technical Skills**

- Python

- MongoDB

- PyMongo

- CRUD database operations

- Database Indexing

- Query validation

- Data-integrity validation

- Partial-update validation

- Query projection

- MongoDB exception handling

- Secure environment configuration

- Database testing

### Enhancement Narrative 

[Read the Database Enhancement Narrative](database-narrative.md)
