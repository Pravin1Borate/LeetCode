# Write your MySQL query statement below


SELECT Id
FROM (
    SELECT a.*, 
           LAG(recordDate) OVER(ORDER BY recordDate) AS prev_date, 
           LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
    FROM weather AS a
)  as b
WHERE temperature > prev_temp AND
DATEDIFF(recordDate, prev_date) = 1