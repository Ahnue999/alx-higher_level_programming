-- Computes the score avarage of all records.
SELECT SUM(`score`)/COUNT(`name`) AS AVARAGE FROM `second_table`
