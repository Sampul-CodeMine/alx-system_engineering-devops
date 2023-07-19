DROP USER IF EXISTS 'replica_user'@'localhost';
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'rep_user_123';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO holberton_user@localhost;
