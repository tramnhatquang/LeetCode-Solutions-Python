#
Write your MySQL query statement below
SELECT co.name AS country
FROM person p
         INNER JOIN country co
                    ON LEFT(phone_number, 3) = country_code

         INNER JOIN calls c
                    ON p.id = c.caller_id
                        OR p.id = c.callee_id
GROUP BY co.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM calls)