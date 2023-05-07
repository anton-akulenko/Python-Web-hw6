select s.fullname, round(AVG(g.grade), 2) as avg_grade  
from grades g 
left join students s on s.id = student_id 
group by s.fullname 
order by avg_grade desc limit 5;
