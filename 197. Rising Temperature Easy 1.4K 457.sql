SELECT A.ID
FROM WEATHER A
         JOIN WEATHER B
              ON (A.RECORDDATE - INTERVAL '1' DAY) = B.RECORDDATE
WHERE B.TEMPERATURE < A.TEMPERATURE