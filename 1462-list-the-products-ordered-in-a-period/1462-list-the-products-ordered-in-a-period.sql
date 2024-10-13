# Write your MySQL query statement below

SELECT product_name
  , SUM(unit) AS unit
FROM Products p
LEFT JOIN Orders o ON o.product_id = p.product_id
WHERE order_date >= "2020-02-01"
  AND order_date <= "2020-02-29"
GROUP BY 1
HAVING SUM(unit) >= 100