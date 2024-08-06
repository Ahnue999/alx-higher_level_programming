-- Computes the score avarage of all records.
SELECT SUM(`score`)/COUNT(`name`) AS avarage FROM `second_table`
