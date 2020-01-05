BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tbl_flags" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ftype"	INTEGER,
	"fcondition"	INTEGER,
	"fevent"	INTEGER,
	"fname"	TEXT,
	"fstatus"	INTEGER NOT NULL,
	FOREIGN KEY("ftype") REFERENCES "tbl_types"("id"),
	FOREIGN KEY("fcondition") REFERENCES "tbl_conditions"("id"),
	FOREIGN KEY("fstatus") REFERENCES "tbl_events"("id")
);
CREATE TABLE IF NOT EXISTS "tbl_events" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fname"	TEXT,
	"fstatus"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "tbl_conditions" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fname"	TEXT,
	"fcode"	TEXT,
	"fstatus"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "tbl_types" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fname"	TEXT,
	"fcode"	TEXT,
	"fstatus"	INTEGER NOT NULL
);
INSERT INTO "tbl_flags" ("id","ftype","fcondition","fevent","fname","fstatus") VALUES (1,1,1,1,'birthday.flg',1);
INSERT INTO "tbl_flags" ("id","ftype","fcondition","fevent","fname","fstatus") VALUES (2,1,1,2,'memday.flg',1);
INSERT INTO "tbl_flags" ("id","ftype","fcondition","fevent","fname","fstatus") VALUES (3,1,1,3,'commday.flg',1);
INSERT INTO "tbl_events" ("id","fname","fstatus") VALUES (1,'День рождения',1);
INSERT INTO "tbl_events" ("id","fname","fstatus") VALUES (2,'День памяти',0);
INSERT INTO "tbl_events" ("id","fname","fstatus") VALUES (3,'Показания счётчиков',0);
INSERT INTO "tbl_conditions" ("id","fname","fcode","fstatus") VALUES (1,'По созданию','on_create',1);
INSERT INTO "tbl_conditions" ("id","fname","fcode","fstatus") VALUES (2,'По удалению','on_delete',1);
INSERT INTO "tbl_types" ("id","fname","fcode","fstatus") VALUES (1,'Сообщение','message',1);
INSERT INTO "tbl_types" ("id","fname","fcode","fstatus") VALUES (2,'Команда','command',1);
COMMIT;
