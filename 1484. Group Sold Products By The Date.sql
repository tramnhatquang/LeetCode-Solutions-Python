# Write your MySQL query statement below
# Use GROUP_CONCAT to group multiple products under one category with a separator, the defualt separator is ','
SELECT 
	sell_date,
	COUNT(DISTINCT product) AS num_sold,
	GROUP_CONCAT(DISTINCT product ORDER BY product) AS products 
FROM Activities
GROUP BY sell_date