-- # Write your MySQL query statement below
SELECT CUSTOMER_NUMBER
FROM ORDERS
GROUP BY CUSTOMER_NUMBER
HAVING COUNT(CUSTOMER_NUMBER) >= ALL (SELECT COUNT(CUSTOMER_NUMBER)
                                      FROM ORDERS
                                      GROUP BY CUSTOMER_NUMBER);

-- This works in case there are more than one customer who have the largest numbers of orders