 CREATE TABLE Users(
ID SERIAL PRIMARY KEY,
Login varchar(30) UNIQUE NOT NULL,
Password varchar(50) NOT NULL,
Email varchar(50) UNIQUE NOT NULL,
Lastname varchar(30),
Firstname varchar(30),
Age int NOT NULL,
Eyes varchar(50) NOT NULL,
Hair varchar(100) NOT NULL,
Height int NOT NULL,
Created timestamp
);
	 
CREATE TABLE Events(
    ID SERIAL PRIMARY KEY,
    event_name varchar(50) NOT NULL ,
    Created timestamp,
	CountOfOptions int NOT NULL DEFAULT 0,
	User_ID int,
	CONSTRAINT FK_User_ID FOREIGN KEY (User_ID)
      REFERENCES Users (ID),
	CONSTRAINT Check_Count_Events CHECK (CountOfOptions >= 0)
);
 
CREATE TABLE Options (
ID SERIAL PRIMARY KEY,
place varchar(100) NOT NULL ,
season varchar(100) NOT NULL,
Created timestamp,
temperature int NOT NULL,
CountOfClothes int NOT NULL DEFAULT 0,
Events_ID int,
	CONSTRAINT FK_Events_ID FOREIGN KEY (Events_ID)
      REFERENCES Events (ID),
	CONSTRAINT Check_Count_Clothes CHECK (CountOfClothes >= 0)
);

CREATE TABLE Clothes(
    ID SERIAL PRIMARY KEY,
    style_name varchar(100) NOT NULL ,
    outwear varchar(50) NOT NULL,
	lowerwear varchar(50) NOT NULL,
	shoes varchar(50) NOT NULL,
	Created timestamp,
	Options_ID int,
	CONSTRAINT FK_Options_ID FOREIGN KEY (Options_ID)
      REFERENCES Options (ID)
);
