# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.state, a.city
from Person p
LEFT JOIN Address a
ON p.personId = a.personId;