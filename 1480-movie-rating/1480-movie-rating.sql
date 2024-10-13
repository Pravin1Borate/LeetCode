# Write your MySQL query statement below

(SELECT name AS results
FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)
UNION ALL
(SELECT title as results
FROM MovieRating JOIN Movies using(movie_id)
WHERE created_at like "%2020-02%" 
GROUP BY title
ORDER BY avg(rating) desc,title
LIMIT 1);