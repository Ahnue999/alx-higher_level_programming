-- lists all records, skipping those without a name;
SELECT `score`, `name` FROM second
	WHERE `name` IS NOT ""
	ORDER BY `score` DESC
