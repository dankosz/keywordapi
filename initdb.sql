CREATE TABLE keywordpubs (
id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, 
keywordid INT(11) NOT NULL, 
objectid VARCHAR(255));

+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| id        | int(11)      | NO   |     | NULL    |       |
| keywordid | int(11)      | NO   |     | NULL    |       |
| objectid  | varchar(255) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
