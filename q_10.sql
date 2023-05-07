select s.fullname as Stud,  t.fullname as Teacher, s2.name as Subj  
from grades g 
left join students s on s.id = g.student_id 
left join subjects s2 on s2.id = g.subject_id  
join teachers t on t.id = s2.teacher_id 
where s.id = 5 and t.id = 7
group by s2.id, s.id, t.fullname;
