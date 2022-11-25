create database if not exists cine;
use cine;

drop table if exists Tickets;
drop table if exists Functions;
drop table if exists Movies;
drop table if exists Users;

-- Movies
create table Movies (
id_movie int primary key, 
title varchar(100) not null,
poster varchar(300) not null,
clasif varchar (5) not null,
created_at datetime 
);

-- Users
Create table Users(
id_user int auto_increment not null,
name_user varchar(40) not null,
last_name varchar(40) not null,
password_user varchar(30) not null,
email varchar(50) not null unique,
phone_number varchar(15) not null,
created_at datetime,
primary KEY(id_user,email)
);

-- Function
Create table Functions (
id_funct int primary key,
ID_movie int not null,
date_funct datetime not null,
created_at datetime,
FOREIGN KEY (ID_movie) REFERENCES Movies(id_movie)
);

-- tickets 
create table Tickets(
id_ticket int auto_increment unique,
ID_USER int not null,
ID_MOV int not null,
ID_FUNC int not null,
seat varchar(3) not null,
created_at datetime,
FOREIGN KEY (ID_MOV) references Movies(id_movie),
foreign key (ID_FUNC) references Functions(id_funct),
foreign key (ID_USER) references Users(id_user),
primary key (ID_FUNC,seat)
);
INSERT INTO Movies VALUES 
(11, "Avatar","https://cdn.shopify.com/s/files/1/0057/3728/3618/products/avatar_pahieuwv_480x.progressive.jpg?v=1662754304", "B12", now()),
(22, "Toy Story 2", "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/f07858b1841afc2cfdc7059d68290e71_d96ae72f-5766-49c2-9f22-b7c7f5ae5f42_480x.progressive.jpg?v=1573585163", "A", now()),
(33, "Ice Age 4", "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/56a36324f2f722d6c11aa96eb0d115a8_550ce8e3-e33f-44c6-8ef6-bb2245ba85e2_480x.progressive.jpg?v=1573587343", "A", now()),
(44, "Spider-man No Way Home", "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/301983133_1072845516765536_7607702103270945846_n_480x.progressive.jpg?v=1665071762", "B", now());

INSERT INTO Functions VALUES
(555,11,'2022-11-21 19:00:00',now()),(777,11,'2022-12-23 21:00:00',now()),(888,11,'2022-12-27 21:00:00',now()),
(763,22,'2022-11-24 14:00:00',now()),(389,22,'2022-11-19 17:00:00',now()),(942,22,'2022-12-21 19:30:00',now()),
(324,33,'2022-12-12 22:00:00',now()),(784,33,'2022-12-02 13:00:00',now()),(467,33,'2022-12-07 14:00:00',now()),
(981,44,'2022-11-29 21:00:00',now()),(849,44,'2022-12-29 20:00:00',now()),(999,44,'2022-12-22 23:00:00',now());



 INSERT INTO Users(name_user, last_name , password_user, email, phone_number, created_at ) VALUES ('EDWIN','CARRANZA','2222','ejemplo1@gmail.com','98874883', now());
-- select Movies.id_movie , Movies.title , Movies.poster , Movies.clasif , Functions.id_funct , Functions.date_funct 
-- from Movies inner join Functions on Movies.id_movie = Functions.ID_movie;
-- INSERT INTO Users(name_user, last_name , password_user, email, phone_number, created_at ) VALUES ('DARCY','HERNANDEZ','11111','ejemplo2@gmail.com','345345343243', now());
INSERT INTO Tickets (ID_USER , ID_MOV , ID_FUNC , seat , created_at) VALUES (1,44,981,'A10',now());     
SELECT * FROM Tickets;
-- DELETE FROM Tickets where Tickets.ID_USER = 2 and Tickets.id_ticket = 3;
-- select Functions.date_funct from Functions inner join Tickets on Functions.id_funct = Tickets.ID_FUNC 
-- where Tickets.id_ticket = 3;

-- SELECT Tickets.id_ticket , Tickets.seat , Functions.id_funct, Functions.date_funct, 
-- Movies.id_movie, Movies.title , Movies.poster , Movies.clasif from Tickets inner join Functions on Tickets.ID_FUNC = Functions.id_funct
-- inner join Movies where Tickets.ID_USER = 2 and Functions.Id_movie = Movies.id_movie