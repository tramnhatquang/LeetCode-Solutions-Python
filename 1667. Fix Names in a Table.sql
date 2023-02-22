# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name,2))) AS "name"
FROM Users
ORDER BY 1;

-- Rememeber susbtring(word, start_position, length) and SQL starts at 1-indexed