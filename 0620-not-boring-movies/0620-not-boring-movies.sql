# Write your MySQL query statement below

SELECT id
  , movie
  , description
  , rating
FROM (
  SELECT a.*
    , CASE
      WHEN id % 2 = 0 THEN 1
      ELSE 0
    END AS odd_flag
  FROM Cinema AS a
) AS b
WHERE odd_flag = 0
  AND description not like '%boring%'
ORDER BY rating DESC
;