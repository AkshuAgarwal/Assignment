/*
Project 21: SQL Queries
*/

-- 1). Write a SQL command to create a Database named 'school'.
CREATE DATABASE `school`;

-- 2). Create a student table with the student id, name, and marks as attributes where the student id is the primary key.
CREATE TABLE `student` (
    `student_id` INT       PRIMARY KEY,
    `name`       CHAR(30),
    `marks`      INT
);

-- 3). Add columns ‘Mobile’ and ‘Sex’ in the table student.
ALTER TABLE `student`
ADD (
    `mobile` BIGINT,
    `sex`    CHAR(10)
);

-- 4). Add column ‘Address’ in the table student.
ALTER TABLE `student`
ADD (`address` CHAR(30));

-- 5). Change the name of column ‘Sex’ to ‘Gender’
ALTER TABLE `student`
CHANGE `sex` `gender` CHAR(10);

-- 6). Delete a column ‘Address’ from table Student.
ALTER TABLE `student`
DROP `address`;

-- 7). Insert the details of 10 new students in the above table.
INSERT INTO `student` (`student_id`, `name`, `marks`, `mobile`, `gender`)
VALUES (1004, 'Reenu', 87, 9910281550, 'FEMALE'),
       (2019, 'Sanya', 94, 7011195462, 'FEMALE'),
       (3897, 'Sarthak', 76, 9876567891, 'MALE'),
       (7652, 'Zoya', 91, 9876453456, 'FEMALE'),
       (2341, 'Vansh', 87, 9876655278, 'MALE'),
       (3456, 'Sarthak', 67, 8798765678, 'MALE'),
       (7856, 'Astha', 89, 9876789678, 'FEMALE'),
       (1267, 'Anshika', 97, 8700522033, 'FEMALE'),
       (3045, 'Deepanshu', 54, 8700999884, 'MALE'),
       (3452, 'Siya', 86, 9988775645, 'FEMALE');

-- 8). Use the select command to get the details of the students with marks more than 80.
SELECT *
FROM `student`
WHERE `marks` > 80;

-- 9). Change the mobile number of any one student.
UPDATE `student`
SET `mobile` = 9988765678
WHERE `student_id` = 3452;

-- 10). Display the details of those students which name start with ‘A’
SELECT *
FROM `student`
WHERE `name` LIKE 'A%';

-- 11). Write output :SELECT LENGTH(NAME), SUBSTR(NAME, 3,3) FROM STUDENT;
SELECT LENGTH(`name`),
       SUBSTR(`name`, 3, 3)
FROM `student`;

-- 12). Write output : SELECT COUNT (DISTINCT GENDER) FROM STUDENT;
SELECT COUNT(DISTINCT `gender`)
FROM `student`;

-- 13). Display a report like ‘Aditya is scored 20 out of 30” for each student. Where Aditya is the name of student and 20 is the marks of Aditya.
SELECT CONCAT(`name`, ' has scored ', `marks`, ' out of 100') AS `REPORT`
FROM `student`;

-- 14). Find the min, max, sum, and average of the marks in a student marks table.
SELECT MAX(`marks`) AS `MAXIMUM MARKS`,
       MIN(`marks`) AS `MINIMUM MARKS`,
       SUM(`marks`) AS `TOTAL MARKS`,
       AVG(`marks`) AS `AVERAGE MARKS`
FROM `student`;

-- 15). Display the Gender, Minimum marks and Maximum Marks Gender wise.
SELECT `gender`,
       MIN(`marks`) AS `MINIMUM MARKS`,
       MAX(`marks`) AS `MAXIMUM MARKS`
FROM `student`
GROUP BY `gender`;

-- 16). Find the total number of students from student table gender wise using group by.
SELECT COUNT(`name`),
       `gender`
FROM student
GROUP BY `gender`;

-- 17). Write a SQL query to order the (student ID, marks) table in descending order of the marks.
SELECT `student_id`,
       `marks`
FROM `student`
ORDER BY `marks` DESC;

-- 18). Delete the details of a student in the above table.
DELETE FROM `student`
WHERE `student_id` = 1004;

-- 19). Delete the table Student.
DROP TABLE `student`;

-- 20). Delete the Database School.
DROP DATABASE `school`;
