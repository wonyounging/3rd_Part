create user 'web'@'%' identified by '1234';
create user 'web'@'localhost' identified by '1234';
flush PRIVILEGES;

grant all privileges on web.* to 'web'@'%';
grant all privileges on web.* to 'web'@'localhost';

CREATE DATABASE myweb;

SHOW DATABASES;

USE myweb;
SHOW TABLES;

SELECT * FROM gs25;
SELECT * FROM temperature;

DESC gs25;

SELECT DISTINCT sido FROM gs25;

ALTER TABLE gs25 ADD seoul CHAR(1) DEFAULT '0';
UPDATE gs25 SET seoul='1' WHERE sido='서울특별시';
SELECT * FROM gs25 LIMIT 100;

ALTER TABLE gs25 ADD male CHAR(1) DEFAULT '0';
UPDATE gs25 SET male='1' WHERE gender='M';
SELECT * FROM gs25 LIMIT 100;