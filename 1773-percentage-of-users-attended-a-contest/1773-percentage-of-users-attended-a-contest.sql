# Write your MySQL query statement below

SELECT r.contest_id
  , ROUND(
    COUNT(u.user_id) * 100 / (
      SELECT COUNT(DISTINCT user_id)
      FROM Users
    )
    , 2
  ) AS percentage
FROM Users u
INNER JOIN Register r ON u.user_id = r.user_id
GROUP BY r.contest_id
order by percentage desc,r.contest_id asc