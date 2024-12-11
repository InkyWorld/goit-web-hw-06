--Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.first_name, s.last_name, sub.name, g.mark FROM students as s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON gr.id = s.group_id
WHERE gr.name = %s AND sub.name = %s



