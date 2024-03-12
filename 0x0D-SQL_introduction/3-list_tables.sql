-- lists all the tables of a database in your MySQL server.
SET @db_name = ?;
USE @db_name;
SHOW TABLES;
