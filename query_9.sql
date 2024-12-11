--Знайти список курсів, які відвідує студент.

SELECT DISTINCT sub.name FROM students as s
JOIN grades as gr ON gr.student_id = s.id
JOIN subjects as sub ON gr.subject_id = sub.id
WHERE s.first_name = %s AND s.last_name = %s