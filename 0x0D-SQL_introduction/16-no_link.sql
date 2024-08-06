-- lists all records, skipping those without a name;
SELECT `score`, `name` FROM second
	WHERE `name` != NULL
	ORDER BY `score` DESC;
