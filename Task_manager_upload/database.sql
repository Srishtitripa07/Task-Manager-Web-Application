create database task_manager;
use task_manager;
CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE,
created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE tasks (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
description TEXT,
due_date DATE,
status ENUM('Pending','In Progress','Completed') DEFAULT 'Pending',
remarks TEXT,
created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
created_by INT,
updated_by INT,

FOREIGN KEY (created_by) REFERENCES users(id),
FOREIGN KEY (updated_by) REFERENCES users(id)
);
INSERT INTO users (name,email)
VALUES (name ,'name@example.com');
