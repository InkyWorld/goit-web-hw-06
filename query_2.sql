--Знайти студента із найвищим середнім балом з певного предмета.

SELECT s.first_name, s.last_name, sub.name, AVG(g.mark) as avg_mark FROM students as s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = %s
GROUP BY s.id, sub.id
ORDER BY avg_mark desc
limit 1;