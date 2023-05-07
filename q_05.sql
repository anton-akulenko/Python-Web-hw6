select t.fullname, s.name as course 
from subjects as s 
left join teachers as t on t.id = s.teacher_id
where t.id = 3
group by t.fullname, s.name;