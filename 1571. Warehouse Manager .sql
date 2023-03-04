#
Write your MySQL query statement below
SELECT name                                 warehouse_name,
       SUM(units * Width * Length * Height) volume
FROM Warehouse W
         LEFT JOIN Products P
                   ON W.product_id = P.product_id
GROUP BY name