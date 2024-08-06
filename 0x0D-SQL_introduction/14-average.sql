-- Computes the score avarage of all records.
SELECT SUM(`score`)/COUNT(`id`) AS AVARAGE FROM `second_table`
