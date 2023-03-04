/* Write your PL/SQL query statement below */
SELECT p.product_id, ROUND(SUM(u.units * p.price) / SUM(u.units), 2) AS average_price
FROM Prices p
         JOIN UnitsSold u
              ON p.product_id = u.product_id
WHERE (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY p.product_id;