CREATE DATABASE HOSPITAL;
USE HOSPITAL;

-- Creating the Patient data table
CREATE TABLE IF NOT EXISTS patient_data (
    Customer_Name varchar(255) NOT NULL Primary key,
    Customer_ID varchar(18) NOT NULL,
    Open_Date DATE NOT NULL,
    Last_Consulted DATE,
    Vaccination_Id char(5),
    Dr_Name char(255),
    State char(5),
    Country char(5),
    DOB DATE,
    Is_Active char(1))
  
);


-- Loading the data from the text file into our Patients table
LOAD DATA INFILE 'C:/Users/Kanak/Desktop/data.txt' 
INTO TABLE patient_data
FIELDS TERMINATED BY '|' --each tuple separated by |
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' -- \n marks the end of a row i.e one patient's data
IGNORE 1 ROWS; -- text file also contains column names so we decide to ignore it