CREATE TABLE IF NOT EXISTS drugs(
  id INTEGER NOT NULL PRIMARY KEY,
  quantity INTEGER NOT NULL,
  for_sale integer not null,
  for_personal_use integer null);

CREATE TABLE event(
  id INTEGER PRIMARY KEY,
  title VARCHAR (100) NOT NULL,
  data VARCHAR(100) NOT NULL);

CREATE TABLE territory(
  id INTEGER PRIMARY KEY,
  title VARCHAR (100) NOT NULL);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(100)  NOT NULL);

CREATE TABLE gang_members(
  id INTEGER PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  surname VARCHAR(100) NOT NULL,
  ranksID INTEGER NOT NULL);

CREATE TABLE accounting(
  id INTEGER PRIMARY KEY,
  eventID INTEGER NOT NULL,
  income INTEGER NOT NULL,
  costs INTEGER NOT NULL,
  drugs VARCHAR(50) NOT NULL,
  FOREIGN KEY (drugs)
      REFERENCES drugs(id)
      ON DELETE SET NULL ON UPDATE NO ACTION,
  FOREIGN KEY (eventID)
      REFERENCES event(id)
      ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE gangs(
  id INTEGER PRIMARY KEY,
  gangs_title VARCHAR (100) NOT NULL,
  district INTEGER NOT NULL,
  FOREIGN KEY (district)
      REFERENCES territory(id)
      ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS users(
  id INTEGER NOT NULL PRIMARY KEY,
  login VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(50) NOT NULL,
  post INTEGER NOT NULL,
    FOREIGN KEY (post)
        REFERENCES post(id)
);


CREATE TABLE share(
  id INTEGER PRIMARY KEY,
  accountingID  INTEGER NOT NULL,
  memberID INTEGER NOT NULL,
  part INTEGER,
  FOREIGN KEY (accountingID)
      REFERENCES accounting(id)
      ON DELETE SET NULL ON UPDATE NO ACTION,
  FOREIGN KEY (memberID)
      REFERENCES gang_members(id)
      ON DELETE SET NULL ON UPDATE NO ACTION);


INSERT INTO post(id, name)
VALUES (1, 'Admin'), (2, 'Director');

INSERT INTO users(id, login, password,post)
VALUES (1, 'admin', 'admin', 1);

INSERT INTO event(title, data)
VALUES ('title', 'data'),('title1', 'data1');

INSERT INTO accounting(eventid, income, costs, drugs)
VALUES ('eventid','income','costs','drugs'),('eventid1','income1','costs1','drugs1');

INSERT INTO share(accountingID, memberID, part)
VALUES ('accountingID', 'memberID', 'part'),('accountingID1', 'memberID1', 'part1');

INSERT INTO gang_members(name, surname, ranksid)
VALUES ('name', 'surname', 'ranksid'),('name1', 'surname1', 'ranksid1');

INSERT INTO territory(title)
VALUES ('title'),('title1');

INSERT INTO gangs(gangs_title, district)
VALUES ('gangs_title', 'district'),('gangs_title1', 'district1');

INSERT INTO drugs(quantity, for_sale, for_personal_use)
VALUES ('quantity', 'for_sale', 'for_personal_use'),('quantity1', 'for_sale1', 'for_personal_use1');