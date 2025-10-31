-- sql
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states name = 'California')
ORDER BY id ASC;
