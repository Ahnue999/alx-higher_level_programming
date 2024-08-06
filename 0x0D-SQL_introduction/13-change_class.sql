-- Delete all records below a certain threshold.
DELETE FROM `second_table`
	WHERE `score` <= 5
