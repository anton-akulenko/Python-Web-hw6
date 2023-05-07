select s.fullname, sbj."name", sg."name", g.grade  
from grades g 
join students s on s.id = g.student_id 
join student_groups sg on sg.id = s.group_id 
join subjects sbj on sbj.id = g.subject_id 
where sg.id = 1 and sbj.id = 4
order by s.fullname;