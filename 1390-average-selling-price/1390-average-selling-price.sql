# Write your MySQL query statement below

SELECT product_id, 
       CASE 
        WHEN ROUND((total_amount / total_units), 2) != 0 THEN ROUND((total_amount / total_units), 2) ELSE 0
        END AS average_price  
FROM (
    SELECT p.product_id, 
           SUM(p.price * u.units) AS total_amount,
           SUM(u.units) AS total_units
    FROM Prices p
    LEFT JOIN UnitsSold u 
           ON p.product_id = u.product_id
          AND u.purchase_date >= p.start_date 
          AND u.purchase_date <= p.end_date
    GROUP BY p.product_id
) AS F
