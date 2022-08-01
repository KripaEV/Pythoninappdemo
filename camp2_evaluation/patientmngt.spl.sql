CREATE DATABASE PMSystem

USE PMSystem

CREATE TABLE Gender(
	gender_no INT IDENTITY PRIMARY KEY,
	gender VARCHAR(20)
)

CREATE TABLE BloodGroup(
	blood_group_no INT IDENTITY PRIMARY KEY,
	blood_group VARCHAR(5)
)

CREATE TABLE Patient(
	patient_id INT NOT NULL PRIMARY KEY IDENTITY,
	patient_name VARCHAR(20) NOT NULL,
	gender_no INT NOT NULL FOREIGN KEY REFERENCES Gender(gender_no),
	age INT NOT NULL,
	blood_group_no INT NOT NULL FOREIGN KEY REFERENCES BloodGroup(blood_group_no)
)

INSERT INTO Gender VALUES
('Male'),
('Female'),
('Transgender'),
('Other')

INSERT INTO BloodGroup VALUES
('A+'),
('A-'),
('B+'),
('B-'),
('AB+'),
('AB-'),
('O+'),
('O-')

SELECT * FROM Gender
SELECT * FROM BloodGroup
SELECT * FROM Patient