--Оцінки студентів у певній групі з певного предмета на останньому занятті.

WITH period_time AS (
    SELECT *
    FROM grades
    where grades.date_of_grade between '2022-08-03' and current_date
)
select s.fullname, sbj."name", sg."name", pt.grade, pt.date_of_grade  
from period_time pt 
join students s on s.id = pt.student_id 
join student_groups sg on sg.id = s.group_id 
join subjects sbj on sbj.id = pt.subject_id 
where sg.id = 3 and sbj.id = 5
order by pt.date_of_grade desc;
