--Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.first_name, t.last_name, sub.name, AVG(gr.mark) FROM teachers as t
JOIN subjects as sub ON sub.teacher_id = t.id
JOIN grades as gr ON gr.subject_id = sub.id
WHERE t.first_name = %s AND t.last_name = %s
GROUP BY sub.name, t.first_name, t.last_name