select t.fullname as Prepod, s2.name as Predmet, round(AVG(g.grade), 2) as Bal  
from grades g 
left join students s on s.id = g.student_id 
left join subjects s2 on s2.id = g.subject_id 
left join teachers t on t.id = s2.teacher_id 
where t.id =3
group by t.fullname,s2.name 
order by Bal desc;
