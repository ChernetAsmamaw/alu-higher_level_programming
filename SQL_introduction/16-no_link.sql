-- lists all records of the table second_table of the database hbtn_0c_0
-- don’t list rows without a name value
-- results should display the score and the name (in this order)
-- records should be listed by descending score
-- the database name will be passed as an argument to the mysql command
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
