SELECT name
FROM (
  SELECT e1.id
    , e1.name
    , COUNT(e2.id) AS reportee
  FROM employee e1
  CROSS JOIN employee e2 ON e1.id = e2.managerId
  GROUP BY 1, 2
) AS b
WHERE reportee >= 5
