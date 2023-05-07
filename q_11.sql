select t.fullname, s.fullname, round(AVG(g.grade), 2) as Bal  
from grades g 
left join subjects sbj ON sbj.id = g.subject_id 
left join students s on s.id = g.student_id 
left join teachers t on t.id = sbj.teacher_id 
where t.id = 3 and s.id = 30
group by t.fullname, s.fullname 
order by Bal desc;
