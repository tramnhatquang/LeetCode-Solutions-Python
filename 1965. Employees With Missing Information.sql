SELECT employee_id
FROM employees
LEFT JOIN salaries
    USING (employee_id)
WHERE salary IS NULL 
UNION
SELECT employee_id
FROM employees
RIGHT JOIN salaries
    USING (employee_id)
WHERE name IS NULL
ORDER BY  employee_id

-- The other way
# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s 
ON e.employee_id = s.employee_id WHERE s.salary IS NULL
UNION
SELECT s.employee_id
FROM Salaries s
LEFT JOIN Employees e
ON e.employee_id = s.employee_id WHERE e.name IS NULL
ORDER BY employee_id; 