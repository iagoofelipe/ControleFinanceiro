USE financeiro;

CREATE TABLE `user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` varbinary(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE `bank` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_bank_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `financeiro`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE `card` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `num` INT NOT NULL,
  `dia_fechamento` INT NOT NULL,
  `dia_vencimento` INT NOT NULL,
  `limite` DECIMAL(10,2) NOT NULL DEFAULT '0',
  `bank_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_card_bank_id`
    FOREIGN KEY (`bank_id`)
    REFERENCES `financeiro`.`bank` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE `registry` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` TINYINT NOT NULL DEFAULT 0,
  `title` VARCHAR(45) NOT NULL,
  `value` DECIMAL(10,2) NOT NULL DEFAULT 0,
  `datetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `description` VARCHAR(45) NULL,
  `user_id` INT NULL,
  `bank_id` INT NULL,
  `card_id` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_registry_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `financeiro`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_registry_bank_id`
    FOREIGN KEY (`bank_id`)
    REFERENCES `financeiro`.`bank` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_registry_card_id`
    FOREIGN KEY (`card_id`)
    REFERENCES `financeiro`.`card` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);