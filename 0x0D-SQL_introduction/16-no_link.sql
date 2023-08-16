-- Lists all records of the table second_table having a name value different from an empty string
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
