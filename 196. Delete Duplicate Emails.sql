
# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
# Do a self join here, and keep the smallest id that has duplicte rows


DELETE p1.*
FROM Person p1, Person p2
WHERE p1.email = p2.email and p1.id > p2.id;
