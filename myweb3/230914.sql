CREATE DATABASE web;

create user 'user'@'%' identified by '1234';
create user 'user'@'localhost' identified by '1234';
flush privileges;

grant all privileges on web.* to 'user'@'%';
grant all privilegewebs on web.* to 'user'@'localhost';

USE web;
SHOW TABLES;
SELECT * FROM shop_product;