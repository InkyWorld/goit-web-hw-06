--Знайти середній бал у групах з певного предмета.

SELECT gr.name, sub.name, AVG(g.mark) as avg_mark FROM groups as gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.name = %s
GROUP BY gr.id, gr.name, sub.id, sub.name
ORDER BY avg_mark DESC
