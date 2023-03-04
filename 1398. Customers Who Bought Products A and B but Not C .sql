-- # Write your MySQL query statement below
select a.customer_id, a.customer_name
from customers a,
     orders b
where a.customer_id = b.customer_id
group by a.customer_id
having sum(b.product_name = "A") > 0
   and sum(b.product_name = "B") > 0
   and sum(b.product_name = "C") = 0