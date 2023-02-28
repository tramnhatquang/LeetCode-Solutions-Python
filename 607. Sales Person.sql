# Write your MySQL query statement below

# no ndeed left join here
select s.name
from Salesperson s
where s.sales_id NOT IN 
    (SELECT o.sales_id
    FROM Orders o
    INNER JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED');
    