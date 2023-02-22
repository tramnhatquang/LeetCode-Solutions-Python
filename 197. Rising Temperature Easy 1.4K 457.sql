Select A.ID
from Weather A
JOIN Weather B
ON (A.recordDate - Interval '1' Day) = B.recordDate
where B.temperature < A.temperature