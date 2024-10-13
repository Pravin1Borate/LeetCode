# Write your MySQL query statement below

WITH StudentInfo AS (
    SELECT 
        id,
        student,
        LAG(student) OVER (ORDER BY id) AS previous_student,
        COALESCE(LEAD(student) OVER (ORDER BY id),student) AS next_student
    FROM Seat
)

SELECT 
    id,
    CASE 
        WHEN id % 2 = 0 THEN previous_student 
        ELSE next_student 
    END AS student
FROM StudentInfo;
