select s2.name, s.fullname, round(AVG(g.grade), 2) as avg_grade  
from grades g 
left join students s on s.id = g.student_id 
left join subjects s2 on s2.id = g.subject_id 
where s2.id = 5
group by s.fullname, s2.name 
order by avg_grade desc
limit 1;
