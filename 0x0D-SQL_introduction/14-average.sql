-- Computes the score average of all records.
-- SELECT SUM(`score`)/COUNT(`name`) AS average FROM `second_table`
SELECT AVG(`score`) FROM second_table;
