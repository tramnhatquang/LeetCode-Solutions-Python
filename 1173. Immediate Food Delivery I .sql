#
Write your MySQL query statement below
SELECT ROUND(((SELECT COUNT(order_date)
               FROM delivery
               WHERE order_date = customer_pref_delivery_date) / COUNT(delivery_id)) * 100, 2) AS immediate_percentage
FROM delivery
;