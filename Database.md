# Steps for creating a MySQL database 


1. Create the Database
   
   Once you're logged into MySQL, create a new database named quiz by executing:

   CREATE DATABASE quiz;

   To confirm that the database has been created, you can list all databases:

   SHOW DATABASES;

   
2. Select the Database
   
   Now, select the quiz database to work with it:

   USE quiz;

   
3. Create Tables in the quiz Database

   You can now create tables in the quiz database. For example, you might want to create a table to store quiz questions.

   Example SQL query to create a questions table:

   CREATE TABLE questions (
       id INT AUTO_INCREMENT PRIMARY KEY,
       question_text VARCHAR(255) NOT NULL,
       option_a VARCHAR(100) NOT NULL,
       option_b VARCHAR(100) NOT NULL,
       option_c VARCHAR(100) NOT NULL,
       option_d VARCHAR(100) NOT NULL,
       correct_answer CHAR(1) NOT NULL
    );

   
4. Insert Data into the Table

   Once the table is created, you can insert data into it. For example, insert a question into the questions table:

   INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_answer)
   VALUES ('What is the capital of France?', 'Paris', 'London', 'Berlin', 'Rome', 'A');

5. Verify Data
   
   To ensure that the data has been inserted correctly, run the following query:

   SELECT * FROM questions;


6. (Optional) Create a User for the Database

   If you'd like to allow other users to access the quiz database, you can create a new user and grant them access:

   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON quiz.* TO 'username'@'localhost';
   FLUSH PRIVILEGES;

   
7. Done!
You have now created a quiz database and a table to store quiz questions. You can continue adding tables for user data, scores, or any other data you need for your project.
