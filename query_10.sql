--Список курсів, які певному студенту читає певний викладач

SELECT DISTINCT sub.name FROM students as s
JOIN grades as gr ON gr.student_id = s.id
JOIN subjects as sub ON gr.subject_id = sub.id
JOIN teachers as t ON sub.teacher_id = t.id
WHERE s.first_name = %s 
        AND s.last_name = %s
        AND t.first_name = %s 
        AND t.last_name = %s