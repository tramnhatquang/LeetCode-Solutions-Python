# Write your MySQL query statement below
# join two tables and use a left join
select customer_id, COUNT(v.visit_id) as count_no_trans
from Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;

