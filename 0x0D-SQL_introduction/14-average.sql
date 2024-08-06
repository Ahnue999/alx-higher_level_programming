-- Computes the score average of all records.
-- SELECT SUM(`score`)/COUNT(`name`) AS average FROM `second_table`
SELECT AVG(`score`) AS `avarage` FROM second_table;
