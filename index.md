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
**Artifact:**: Course Planner

**Course:** CS 300: Data Structures and Algorithms 
The Course Planner project was made in CS 300 DSA: Analysis and Design to store course information and allow the user to view the course list or search for a specific course and its prerequisites. I chose this artifact because when I originally completed the course, I was still new to sorting and searching algorithms in C++. Going back to this project allowed me to look at the same program again with more experience and think more carefully about how the data structure and search algorithm work together.

### Original Artifact
The original Course Planner stored the course objects in a vector and then searched through the courses using a linear search. The program would check the courses one by one till it came across the user's request. When making this project, I was still trying to learn about different searching and sorting techniques in C++; so the linear search was easier for me to understand and implement. When I look back at it now, I can see how this approach works for a small amount of course data, but it would require more searching as additional courses were added and would make the program slower. The original version also used a raw pointer for the data structure and had limited input validation and error handling. These were areas I wanted to go back to because I now had a better understanding of algorithm efficiency, memory management, and how the program could handle incorrect user input.

### Enhanced Artifact
One of the main improvements I made during this course, I replaced the linear search with a binary search. The original linear search had a time complexity of O(n), while the binary search reduces the search time to O(log n). I also had to make sure the course data was sorted because binary search depends on the data being in order. For this part, I used a lambda comparator with the vector to organize the courses by course number.

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

