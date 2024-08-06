-- Computes the score average of all records.
-- SELECT SUM(`score`)/COUNT(*) AS average FROM `second_table`
SELECT AVG(`score`) AS `average` FROM second_table;
