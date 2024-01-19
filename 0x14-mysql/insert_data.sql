CREATE SCHEMA IF NOT EXISTS `tyrell_corp`;

CREATE TABLE IF NOT EXISTS `tyrell_corp`.`nexus6`(
   `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
   `name` VARCHAR(255) NOT NULL
);
INSERT INTO `tyrell_corp`.`nexus6` (`name`) VALUES ('Leon');
GRANT SELECT ON `tyrell_corp`.* TO 'holberton_user'@'localhost';
