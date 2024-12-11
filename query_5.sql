--Знайти які курси читає певний викладач.

SELECT sub.name, t.first_name, t.last_name FROM teachers as t
JOIN subjects as sub ON t.id = sub.teacher_id
WHERE t.first_name = %s AND t.last_name = %s
