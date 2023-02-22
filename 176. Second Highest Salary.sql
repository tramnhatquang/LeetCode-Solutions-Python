# Write your MySQL query statement below
select 
    (SELECT DISTINCT SALARY
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary;
