// ProjectTwo.cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <unordered_map>

using namespace std;

//Need to create a structure for course information
struct Course {
	string courseNum;
	string courseTitle;
	vector<string>prerequisites;

// Display course information function
	void displayDetailed() const {
		cout << courseNum << ", " << courseTitle << endl;
		cout << "Prerequisites: ";
		if (prerequisites.empty()) {
			cout << "None";
		}
		else {
			for (const auto& prereq : prerequisites) {
				cout << prereq << " ";
			}
		}
		cout << endl;
	}
};

// Interface for data structure
class StructData {
public: 
	virtual bool loadCourses()= 0;
	virtual void printCourses() const = 0;
	virtual void printCourseInfo(const string& courseNum) const = 0;
	virtual void sortCourses() = 0;
};

// Class for using vector data structure
class VectorStructData : public StructData {
public:
	vector<Course> courses;

	bool loadCourses() override {
		vector<Course>hardcodedCourses = {
			{"CSCI100", "Introduction to Computer Science", {}},
			{"CSCI101", "Introduction to Programming in C++", {"CSCI100"}},
			{"CSCI200", "Data Structures", {"CSCI101"}},
			{"CSCI301", "Advanced Programming in C++", {}},
			{"CSCI300", "Introduction to Algorithms", {"CSCI200", "MATH201"}},
			{"CSCI350", "Operating Systems", {"CSCI300"}},
			{"CSCI400", "Large Software Development", {"CSCI301", "CSCI350"}},
			{"MATH201", "Discrete Mathematics",{}},
		};
			courses = hardcodedCourses;
		return true;
	}

	// Print all courses
	void printCourses() const override {
		cout << "Here is a sample schedule:" << endl;
		for (const auto& course : courses) {
			cout << course.courseNum << ", " << course.courseTitle << endl;
		}
	}

	// Search and print a specific course's info
	void printCourseInfo(const string& courseNum) const override {
		for (const auto& course : courses) {
			if (course.courseNum == courseNum) {
				course.displayDetailed();
				return;
			}
		}
		cout << "Course not found." << endl;
	}

	// Alphanumerically sort the courses
	void sortCourses() override {
		sort(courses.begin(), courses.end(), [](const Course& a, const Course& b) {
			return a.courseNum < b.courseNum;
			});
	}
};


// Display Main
void displayMenu() {
	cout << "1. Load Data Structure." << endl;
	cout << "2. Print Course List." << endl;
	cout << "3. Print Course." << endl;
	cout << "9. Exit" << endl;
}

int main() {
	StructData* ds = new VectorStructData();   //easily switch data structures
	int choice;
	cout << "Welcome to the course planner." << endl;
	ds->loadCourses();

	do {
		displayMenu();
		cout << "What would you like to do? ";
		cin >> choice;

		switch (choice) {
		case 1:
				cout << "Courses loaded successfully." << endl;
			break;

		case 2:
			ds->printCourses();
			break;

		case 3: {
			string courseNum;
			cout << "What course do you want to know about?";
			cin >> courseNum;
			ds->printCourseInfo(courseNum);
			break;
		}

		case 9:
			cout << "Thank you for using the course planner!" << endl;
			break;

		default:
			cout << choice << " is not a valid option." << endl;
		}
	} while (choice != 9);

	delete ds;
	return 0;
}
