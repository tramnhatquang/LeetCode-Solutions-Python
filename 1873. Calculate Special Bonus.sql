-- # Write your MySQL query statement below
SELECT employee_id,
	   CASE
		   WHEN MOD(employee_id, 2) = 1 AND name NOT LIKE 'M%' THEN salary
		   ELSE 0
		   END AS bonus
FROM Employees
ORDER BY 1;


-- The other way
SELECT employee_id, if(employee_id % 2 = 0 OR name LIKE 'M%', 0, salary) AS bonus
FROM Employees
ORDER BY employee_id