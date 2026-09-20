select id, case when p_id is null then 'Root'
                when p_id is not null and 
                -- not exists(select Tree1.id, Tree1.p_id, Tree2.id, Tree2.p_id from Tree Tree1 join Tree Tree2 on Tree1.p_id = Tree2.id) then 'Inner'
                exists(select 1 from Tree t2 where t2.p_id = Tree.id) then 'Inner'
                else 'Leaf'
                end as type
from Tree; 