# Computer Science ePortfolio
**By Natalie Fenton**

Computer Science | Software Engineering Concentration

---

## Professional Self-Assessment

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

## Databases 

