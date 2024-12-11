--Знайти список студентів у певній групі.

SELECT g.name, s.first_name, s.last_name FROM students as s
JOIN groups g ON s.group_id = g.id
WHERE g.name = %s