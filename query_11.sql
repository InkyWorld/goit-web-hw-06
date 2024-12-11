-- Середній бал, який певний викладач ставить певному студентові.

SELECT AVG(gr.mark) FROM students as s
JOIN grades as gr ON gr.student_id = s.id
JOIN subjects as sub ON gr.subject_id = sub.id
JOIN teachers as t ON sub.teacher_id = t.id
WHERE s.first_name = %s 
        AND s.last_name = %s
        AND t.first_name = %s 
        AND t.last_name = %s