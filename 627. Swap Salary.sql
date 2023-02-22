# Write your MySQL query statement below
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;

-- The other way
# Write your MySQL query statement below
UPDATE salary set sex = if (sex ='m', 'f', 'm');