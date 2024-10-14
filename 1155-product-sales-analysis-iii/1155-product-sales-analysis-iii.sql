SELECT
    product_id,
    year as first_year,
    quantity,
    price
FROM
    Sales s
where
    (product_id, year) in (
        SELECT product_id,
        MIN(year) AS year
        FROM
            Sales
        GROUP BY
            product_id
    )