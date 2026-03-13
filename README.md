# Task-Manager-Web-Application
It is a web-based system that helps users manage their tasks. Users can create, track, update, and delete tasks easily.
## Main Features Being Built:
#### 1. Create Task
User can add a new task with:
•	Title
•	Description
•	Due Date
•	Status
#### 2. View Tasks
All tasks are displayed in a table format on the dashboard.
Example columns:
•	ID
•	Title
•	Description
•	Due Date
•	Status
•	Actions (Edit / Delete)
•	Remarks 
•	Created_by
•	Updated_by
#### 3. Edit Task
User can update:
•	Title
•	Description
•	Due Date
•	Status (Pending / In Progress / Completed)
#### 4. Delete Task
User can remove a task from the system.

#### 5.Search Task
User can search tasks using the title.
Technologies Used in Your Project
Backend
•	Python
•	Flask
Database
•	MySQL
Frontend
•	HTML
•	Bootstrap
•	CSS
### System Flow
User
 ↓
Web Interface (HTML + Bootstrap)
 ↓
Flask Backend (Python)
 ↓
MySQL Database
 ↓
Tasks Stored and Retrieved


### Database Design Explanation
The Task Manager application uses a relational database to store and manage tasks efficiently. The system maintains a table that stores information such as task title, description, due date, and status. This design ensures data consistency, easy retrieval, and efficient task management.
The database is implemented using MySQL, and the application interacts with it through the Flask backend using SQL queries
 
### Data Dictionary
Field Name	Data Type	Description	Constraint
id	INT	Unique task identifier	Primary Key, Auto Increment
title	VARCHAR (255)	Title of the task	Not Null
description	TEXT	Detailed task description	Nullable
due_date	DATE	Task deadline	Nullable
status	ENUM ('Pending', ‘Progress', 'Completed')	Task progress state	Not Null



##### Code First or Database First Approach
This project follows the Database First Approach.
The database structure was designed first using MySQL, and then the Flask application was developed to interact with the database.
Steps followed:
1.	Database and table were created in MySQL.
2.	Table schema was defined using SQL.
3.	Flask application was connected to the database.
4.	CRUD operations (Create, Read, Update, Delete) were implemented using SQL queries
#### Structure of the Application
The Task Manager application follows the Model–View–Controller (MVC) architecture using server-side rendering. The system uses Flask as the backend framework, HTML templates for the user interface, and MySQL for database storage.
#### Frontend Structure
The frontend of the Task Manager application is designed as a web-based user interface that allows users to interact with the system through a browser. The frontend is responsible for displaying tasks, collecting user input, and sending requests to the backend server.
The user interface is developed using HTML, CSS, and Bootstrap, which provide a responsive and user-friendly design.
#### Environment Details and Dependencies
The Task Manager application is developed using Python Flask framework with MySQL database. The following environment and dependencies are required to run the project.
Component	Version / Tool
Operating System	Windows 
Programming Language	Python 3.10
Backend Framework	Flask
Database	MySQL
Frontend	HTML, CSS, Bootstrap
Package Manager	pip
Required Python Libraries
The following Python packages are required:
Library	Purpose
1.Flask	Web framework used to build the application
 Download or Clone the Project
•	Download the project folder from the repository or copy the source code.
•	Place the project folder on your local system.
Open the Project Folder
•	Open the project folder in your code editor.
 Create a Virtual Environment
•	Create a Python virtual environment to manage dependencies.
python -m venv venv
 Activate the Virtual Environment
For Windows:
venv\Scripts\activate
 Install Required Dependencies
•	Install the necessary Python libraries using pip.
 Setup the Database
•	Open MySQL and create a new database.
               CREATE DATABASE task_manager;
•	Create the tasks table inside the database.
Configure Database Connection
•	Open app.py
Verify Project Structure
Ensure the project contains the following folders and files:
•	app.py
•	templates/
•	static/
•	requirements.txt
Save and Prepare the Application
•	Ensure all dependencies are installed.
•	Confirm database connection is working.


