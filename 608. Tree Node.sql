# Write your MySQL query statement below
# Observation:
#  - Root node does not have a parent (p.id is null)
#  - Inner node have a parent node is NOT NULL and is a parent of other nodes
#  - Leaf node have a parent node is NOT NULL and not a parent of other nodes

# We can think of using a flow control
SELECT id AS 'Id',
    CASE
        WHEN tree.id = (SELECT atree.id from Tree atree WHERE atree.p_id IS NULL) THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM Tree atree) THEN 'Inner'
        ELSE 'Leaf'
    END AS 'Type'
FROM Tree;

-- Better solution
select id,
(case 
 when p_id is null then 'Root'
 when id in (select p_id from tree where p_id is not null) then 'Inner'
 else 'Leaf' end) as Type
from tree
group by id;