# Software Design & Engineering Enhancement Narrative

**Artifact:** Python CRUD Module

**Course:** CS 340: Client/Server Development
Milestone Two Narrative

For artifact one in my software design and engineering enhancement, I was working on the Python CRUD module that was a project in my previous class, CS 340: Client/Server Development. The purpose of this project was to make it perform CRUD (Create, Read, Update, Delete) operations that worked with a MongoDB database. I realized this original version was developed in Codio’s sandbox environment, and I had to switch from a preconfigured sandbox to a real database (MongoDB). The original artifact had shown some basic CRUD functions but was missing modularity, logging, validation, secure coding, and real-world database setup. I have selected this for my enhancement in the capstone so that I can demonstrate my foundation in backend skills: having a database connected to an application and then being able to perform structured operations on stored data.
	
I wanted this artifact on my ePortfolio because I have confidence to demonstrate and explain my mindset on software engineering, backend development, database integration, and having secure, maintainable code. Making artifact improvements has pushed me to finally explore outside of the Codio environment and into a real MongoDB Community Server installation on my own computer. Included: 
	
•	Installing and running MongoDB as a local service
•	Instead of Codio’s no-auth sandbox, had to use actual authentication
•	Created a root admin user and a project-specific AAC user
•	Built safe connections when strings use environment variables
•	Updated the CRUD module to use .env
•	Added logging to track and debug in the structure
•	Implemented validation and error handling 

Some of these enhancements show my ability to work in real backend systems, secure database access, and implement industrial software engineering practices. This improved artifact will be closer to standards in the computer science field and show my readiness for real-world application work. 

With these enhancements, I have shown explanations and demonstrations in progress to several outcomes in the Computer Science program: 
•	Based on my three categories, I have inputted secure database authentication, code layout improvement, added logging, and implemented validation. With these changes, this will show my ability to use well-known techniques and tools to give value through improved backend functionality. 
•	Having a security mindset is like when I moved from Codio’s no-auth environment to a secure local MongoDB installation; I needed to have authentication and user roles. and connection security. I had to make separate admin and project users, which made me acknowledge the design was specifically chosen to reflect awareness of security.
•	In the algorithmic principles and problem-solving, I have demonstrated debugging authentication failures, restructuring logic for updates, and input validation. 
•	Adds professional communication since the narrative and enhancements show how the artifact is explained and demonstrated clearly. 
With these outcomes planned from Module One, I have met these requirements in software engineering and secure design so far. I acknowledge I do not need major updates, but being able to improve the database authentication and configurations has been my stronger suit in my artifact than I had originally thought. 

Going through this enhancement definitely required more work on my part, but it was mainly due to noticing that my past classes had not taught me the full process of installing and configuring MongoDB locally. I had to backtrack in my CS-340 course and realized I had used Codio’s sandbox with no authentication, no user creation, and no local installation. I am currently taking my Full-Stack Development course, and we are now using mock JSON data instead of a real database; I had yet to learn how to connect an application to a real MongoDB server, which made it a struggle for me.  

I was testing my enhanced CRUD module with my unit tests at the time, and when I ran the tests, it would say ‘no authentication connection’.  I did research why it was not connecting till I found out that my local machine did not have MongoDB installed and that the Codio environment I once had for my project was no longer available. I learned how the MongoDB Community Edition handles authentication, starts with zero users, and has a bypass mode that is required to create the initial admin account. I had to make both the root admin and the AAC user, configure environment variables, and update my connection logic to make sure it functioned smoothly. This was completely new to me, and one of my most challenging ones in order to get the connection with MongoDB. However, I had learned throughout the debugging that I needed to have the right authentication and connection to the right strings; made me troubleshoot through multiple layers of the system. 

Another one I had trouble with the most was implementing the environment variables due to their setup at first. My ‘.env’ did not match the names from the CRUD module, which caused Python to load ‘None’ for every variable, and my connection string came out: mongodb://None:None@None:None. This caused MongoDB to reject it and send out errors. I first noticed I had used the wrong variable names and had to update the names in my ‘.env’ file from ‘USER to DB_USER. It still returned None after I ran a check, and then found out that the VS code had been running my test from a different working directory (so it couldn’t find my .env file). I added in ‘load_dotenv(dotenv_path=”.env”) to force Python to load my file from my project folder and then verified my fix by running again: .env loaded correctly, and the variables returned real values. I was able to learn from this about securing configuration and designing environment-based applications. 

