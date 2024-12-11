-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.first_name, s.last_name, AVG(g.mark) as avg FROM students as s
JOIN grades as g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg DESC
LIMIT 5;