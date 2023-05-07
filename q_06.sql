select s.fullname 
from students s 
left join student_groups sg on sg.id = s.id
where s.group_id = 1;