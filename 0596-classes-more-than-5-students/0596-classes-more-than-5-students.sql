# Write your MySQL query statement below

SELECT class
FROM Courses
group by class
Having count(student) >= 5
