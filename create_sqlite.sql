-- database: database.db
CREATE TABLE `user` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `username` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL
);

CREATE TABLE `bank` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `name` TEXT NOT NULL,
    `description` TEXT,
    `user_id` INTEGER NOT NULL REFERENCES `user`(`id`)
);

CREATE TABLE `card` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `num` INTEGER NOT NULL,
    `dia_fechamento` INTEGER NOT NULL,
    `dia_vencimento` INTEGER NOT NULL,
    `limite` NUMERIC NOT NULL DEFAULT 0,
    `bank_id` INTEGER NOT NULL REFERENCES `bank`(`id`)
);

CREATE TABLE "registry" (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    `type` INTEGER NOT NULL DEFAULT 0, 
    `title` TEXT NOT NULL, 
    `value` TEXT NOT NULL DEFAULT 0, 
    `datetime` TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP), 
    `description` TEXT, 
    `user_id` INTEGER NOT NULL REFERENCES `user`(`id`),
    `bank_id` INTEGER REFERENCES `bank`(`id`),
    `card_id` INTEGER REFERENCES `card`(`id`)
);