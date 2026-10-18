// ProjectTwo.cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.

// This project is a simple course planning system that has a stored list of computer science courses that
//         include prerequisites; user can see them displayed and are able to look up detailed information 
//         about any course. 


#include <memory>  // This will open access to C++ smart pointers (unique_ptr, make_unique, etc).
                   // In addition, since its modern C++ it will not use raw new/delete for saftey reason.

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

//The course structure will hold all info related to a single course.
// makes course data organized and easy to manage.
struct Course {
	string courseNum;
	string courseTitle;
	vector<string>prerequisites;

// Display course information function
	void displayDetailed() const {   // Prints details and will NOT be modified since it read-only.
		cout << courseNum << ", " << courseTitle << endl; // Prints
		cout << "Prerequisites: ";   // Will show list if there is Prerequisites.
		if (prerequisites.empty()) { // Verifies if there is a preprequisites vector has zero elements.
			                         // save time from printing an empty list.
			cout << "None";          // if empty will display "None".
		}
		// If prerequisite is not empty, then it will print each individually. 
		else {
			// Range -based loop; goes through every item in this container, one at a time. 
			for (const auto& prereq : prerequisites) {
				cout << prereq << " ";
			}
		}
		cout << endl; // Prints out newline to keep separate course's output from the next one.
	}
};

// Interface for data structure (what functions must exist).
// Note: Here can change data structures (vector, map, tree) without changing the rest of program.
class StructData {
public: 
	
	// Any class that shows a course data structure will be in these four sections.
	// enables polymorphism: child classes override this function.
	virtual bool loadCourses()= 0;
	virtual void printCourses() const = 0;
	virtual void printCourseInfo(const string& courseNum) const = 0; // uses const string& to avoid copying a string.
	virtual void sortCourses() = 0; // sort the course list alphabetically.
};

// Class for using vector data structure (implements the interface). 
class VectorStructData : public StructData {
public:
	vector<Course> courses; // Stores all course objects (actual data structure). 
	                        // Great for small datasets for a dynamic array.

	bool loadCourses() override {          // implements the interfact function and overrides the base class version.
		vector<Course>hardcodedCourses = { // temporary hold on all data courses.
        //Note: acceptable hardcoded unless if I have to load it from a file. 

			// Note: {} represent prerequisities slot; if empty that means there is none.
			{ "CSCI100", "Introduction to Computer Science",{} },
			{ "CSCI101", "Introduction to Programming in C++",{ "CSCI100" } },
			{ "CSCI200", "Data Structures",{ "CSCI101" } },
			{ "CSCI301", "Advanced Programming in C++",{} },
			{ "CSCI300", "Introduction to Algorithms",{ "CSCI200", "MATH201" } },
			{ "CSCI350", "Operating Systems",{ "CSCI300" } },
			{ "CSCI400", "Large Software Development",{ "CSCI301", "CSCI350" } },
			{ "MATH201", "Discrete Mathematics",{} },
		}; // end of initializer list.
		courses = hardcodedCourses; // Copies into the class's courses number (class owns the full dataset now).
		return true; // successfully loaded.
	}

	// Print all courses
	void printCourses() const override {     // implements the interface function (read-only)
		cout << "Here is a sample schedule:" << endl;
		for (const auto& course : courses) { // range-based loop; goes through each course object in vector.
			cout << course.courseNum << ", " << course.courseTitle << endl;
		}
	}

	//_______________________________________________________________________________________________________________________________________
		// New: updated input
		// Switching from Linear search O(n) to Binary Search O(log n) 
		// Instead of checking ALL the courses, this will sort through fewer courses (logically).
		// Improve perfomance immmensely, and separate the search logic. 
	int binarySearch(const string& courseNum) const {

		// The search works by keeping the range narrow of the entire vector. 
		int left = 0;  //start
		int right = courses.size() - 1; //end (index ends at 0-7 instead of 8, prevents out-of-bounds memory. 

		// This will keep searching if the elements are valid; if not it will stop. 
		while (left <= right) {

			// Core to Binary Search, will check the middle first.
			// prevents overflow and shrink down search without skipping elements. 
			int mid = left + (right - left) / 2;

			// if the middle course is the one we want, halt searching and then return its index.
			// if we found it in the middle, saves time from the search.
			if (courses[mid]                 // looks at middle course number.
				.courseNum == courseNum) {   // check course number and then compare to user typed (target).
				return mid;
			}

			// Process to making this work is by cutting the search space in half. 
			// Note: left = 0 and right = 7. 
			else if (courseNum < courses[mid].courseNum) {  // verifies alphabetical order (in this case user wants before the middle; less).
				right = mid - 1;                            // shrink search processes by moving the right boundary to left (ignores right side).
			}

			// Next, do the opposite where user wants the element after middle (greater) .
			else {
				left = mid + 1; // again, shrink search but now moving the left boundary to right (ignore left side).
			}
		}
		// loop will end if course is not found.
		return -1;
	}

	// Now Binary Search needs a certain printCourseInfo to search and print. 
	// connects the binary search to rest of program and separate from function (organized). 
	// This section only handles printing only.
	void printCourseInfo(const string& courseNum) const override {

		// Adding a second layer of protection if course does not exist in data structure: Exception handling.
		// try/catch block will prevent crashes and logic stays organized. 
		// this will run code that may fail.
		try{
		// Call the binary search function and looks for typed number by user in sorted vector.
		int index = binarySearch(courseNum);

		// if course(index) is not -1, then course exists
		if (index != -1) {
			courses[index].displayDetailed(); // will print all of the course info
		}
		// if course does not exist, will throw an exception.
		else {
			throw runtime_error("Course not found."); // sends message to user.
		}
	}
	// catches the thrown error; prevent it from crashing. 
	catch (const exception& e) {
		cout << "Error: " << e.what() << endl; // print a message to the user. 
	}
}

// Input Validation ( deals with errors BEFORE running it. bad input)
// Error handling   ( deals with errors AFTER happening. runtime failures)
// Modularity       ( being able to apply separation of concerns; keeping functions organized and separate.
//_________________________________________________________________________________________________________________________________________


	// Before using binary search, my data needs to be sorted (alphabetically). 
	void sortCourses() override {
		sort(courses.begin(), courses.end(), // pointer to the first element and pointer to the last element (range to sort through).
			[](const Course& a, const Course& b) {  // compare two Course objects (lambda function).
			return a.courseNum < b.courseNum; // comparison rule; sorts the whole vector alphabetically. 
			}); // end of lambda and sort call
	}
};


//-----------------------------------------------------------------------------------------------------------------------------------------
// New input:
// Input Validation 
// Checks if the user's course input is valid (true or false).
bool isValidCourse(const string& input) {

	// Verify the user's input length (not too short or not too long). 
	// if less than 4 OR more than 8; invalid. 
	if (input.length() < 4 || input.length() > 8) {
		return false; // halt, input is not valid. 
	}
	// loops to check each character is correct. 
	// Note: isalnum will ensures that each character is a letter or number. 
	for (char c : input) {     // verify user's input of each character (one by one); stored in c during loop.
		if (!isalnum(c)) {     // if not a letter or number...
			return false;      // errors for this will be spaces, symbols, dashes, etc.
		}
	}
	return true; // stop when input is wrong. 
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Display Main
void displayMenu() {
	cout << "1. Load Data Structure." << endl;
	cout << "2. Print Course List." << endl;
	cout << "3. Print Course." << endl;
	cout << "9. Exit" << endl;
}

int main() {
	// The smart pointer will own one object and will be created without using 'new' for safety.
	// Results in automatically freeing memory when main() ends; no deletion needed.
	unique_ptr<StructData> ds = make_unique<VectorStructData>();
	
	// variable to store the user's menu selection.
	int choice;
	cout << "Welcome to the course planner." << endl;
	
	// smart pointer will still behave like a normal pointer when using -> .
	// loads all hardcoded course data into the vector. 
	ds->loadCourses();

	// Loop will keep running till user chooses option 9 to Exit. 
	do {
		displayMenu(); //show options.
		cout << "What would you like to do? ";
		cin >> choice; // prompts for user input.

		// Handles different menu options, and clearner than if statements. 
		switch (choice) {
		// loads the data structure.
		case 1:
				cout << "Courses loaded successfully." << endl;
			break;
        // prints all of the courses.
		case 2:
			ds->printCourses();
			break;
		// print one course.
		case 3: {
			string courseNum;
			cout << "What course do you want to know about?";
			cin >> courseNum;  // asks user for the course number. 

			//------------------------------------------------------------------------------------------------------------------------------
			// Updated input: 
			// Checks if the course number was typed in properly by user before program searches for it.
			// verifies input: lengths and character. prevents unpredictable behavior and catch bad input early.
			// mainly for case 3 since it is a certain part of the program where the user enters a course number.
			if (!isValidCourse(courseNum)) {
				cout << "Invalid course format. Please try again." << endl; // user gets feeback if its typed wrong.
			}
			// includeds exception handling for course not found. 
			ds->printCourseInfo(courseNum);
			break;
		}
			//------------------------------------------------------------------------------------------------------------------------------
		// exit program.
		case 9:
			cout << "Thank you for using the course planner!" << endl;
			break;
		// If user use any number that is not 1, 2, 3, or 9. (prevents crashing). 
		default:
			cout << choice << " is not a valid option." << endl;
		}
	} while (choice != 9); //loops continues till users enter 9 (menu keeps showing till then).

	return 0; // Ends the program 
}
