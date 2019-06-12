BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `PARTIDA` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Turno`	INTEGER,
	`Nombre`	TEXT,
	`Uno`	INTEGER,
	`Dos`	INTEGER,
	`Tres`	INTEGER,
	`Cuatro`	INTEGER,
	`Cinco`	INTEGER,
	`Seis`	INTEGER,
	`Escalera`	INTEGER,
	`Full`	INTEGER,
	`Poker`	INTEGER,
	`Generala`	INTEGER,
	`2Generala`	INTEGER
);
INSERT INTO `PARTIDA` VALUES (1,0,'Bruno',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1);
COMMIT;
