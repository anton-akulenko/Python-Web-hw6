select sg.name, sbj.name, round(AVG(g.grade), 2) as avg_grade  
from grades g 
join students s on s.id = g.student_id 
join  subjects sbj on sbj.id = g.subject_id
join student_groups sg on sg.id = s.group_id 
where sbj.id = 1
group by sg.name, sbj.name 
order by avg_grade desc
limit 3;
