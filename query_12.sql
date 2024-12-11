-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT s.first_name, s.last_name, sub.name, g.mark, g.date_of_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE gr.name = 'Group-04-Б' AND sub.name = 'Що'
	AND g.date_of_grade = (select MAX(date_of_grade) from grades WHERE student_id = g.student_id
    AND subject_id = g.subject_id)
ORDER BY s.last_name, s.first_name;