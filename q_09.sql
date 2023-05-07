select s.fullname, s2.name as Predmet  
from grades g 
left join students s on s.id = g.student_id 
left join subjects s2 on s2.id = g.subject_id  
where s.id = 45
group by s2.id, s.id ;
