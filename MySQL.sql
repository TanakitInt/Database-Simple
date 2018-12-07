CREATE TABLE customer(
	cus_id 		INT(10) PRIMARY KEY,
	name		VARCHAR(255) NOT NULL,
	sex			ENUM('Male','Female') NOT NULL,
	cus_phone	CHAR(10) NOT NULL,
	civ_id		CHAR(13) NOT NULL);

INSERT INTO customer
VALUE (0000000001, 'Amporn Kaewburesai', 'Female', '0864703150', '2033088984507'),
(0000000002, 'Nontawat Kongsangchai', 'Male', '0902258160', '8160644328309'),
(0000000003, 'Pim Jetatikarn', 'Female', '0893071880', '2034016726901'),
(0000000004, 'Petch Somwan', 'Male', '0847176920', '5827344693902'),
(0000000005, 'Sangrawee Sripituksakul', 'Female', '0837899960', '4233141254606'),
(0000000006, 'Sinee Narkbunnum', 'Female', '0962309430', '5098881372208'),
(0000000007, 'Suttida Rojumanong', 'Female', '0829387000', '6371882263401'),
(0000000008, 'Chompoo Sirisopa', 'Female', '0902203730', '75934988214010'),
(0000000009, 'Intira Ornlamai', 'Female', '0954768010', '3421959185307'),
(0000000010, 'Pongrit Sakda', 'Male', '0954980750', '21192457309011'),
(0000000011, 'Sarawut Suntornnitikul', 'Male', '0840967480', '2332772265203'),
(0000000012, 'Tuksin Kaewburesai', 'Male', '0945268730', '67857673501011'),
(0000000013, 'Prakorb Nimitwanitch', 'Male', '0947761730', '6445460574507'),
(0000000014, 'Vit Sakda', 'Male', '0810540720', '6624989917506'),
(0000000015, 'Pongrit Kadesadayurat', 'Male', '0904152710', '6149741955802'),
(0000000016, 'Tidarat Leekpai', 'Female', '0981808970', '8959982669904'),
(0000000017, 'Chaowalit Paowsong', 'Male', '0824677980', '8759659179307'),
(0000000018, 'Amporn Pornpipatpong', 'Female', '0859422800', '5556758920603'),
(0000000019, 'Udom Bunyasarn', 'Male', '0926255830', '8980304748606'),
(0000000020, 'Orapan Chaisurivirat', 'Female', '0825293650', '4642473039302'),
(0000000021, 'Suwattanee Kaewburesai', 'Female', '0848912620', '3922890306301'),
(0000000022, 'Surat Atitarn', 'Male', '0836542870', '3868154523504'),
(0000000023, 'Niwat Nimitwanitch', 'Male', '0805523150', '5741646451303'),
(0000000024, 'Prasopchai Kaouthai', 'Male', '0888633140', '21048555915011'),
(0000000025, 'Tidarat Vipavakit', 'Female', '0930341620', '5952730041209'),
(0000000026, 'Akkarat Sripituksakul', 'Male', '0916745800', '58274675609011'),
(0000000027, 'Pairote Atitarn', 'Male', '0997048920', '3736221907606'),
(0000000028, 'Nuntida Parnthong', 'Female', '0898048210', '42108582400010'),
(0000000029, 'Nontawat Lertkunakorn', 'Male', '0884839070', '6323538200307'),
(0000000030, 'Songpole Kaouthai', 'Male', '0953688070', '4918988637504');

CREATE TABLE staff(
	staff_id 	INT(5) PRIMARY KEY,
	name		VARCHAR(255) NOT NULL,
	age			INT(2) NOT NULL,
	staff_phone VARCHAR(10) NOT NULL,
	sex			ENUM('Male','Female') NOT NULL,
	role		VARCHAR(255),
	salary		INT(8));

INSERT INTO staff
VALUE (00001, 'Nopparat Shinawatra', '36', '0974702330', 'Male', 'Security', '20400'),
(00002, 'Arthit Kurusarttra', '39', '0972147260', 'Female', 'Cook', '27800'),
(00003, 'Wirasak Kongpaisarn', '30', '0912448190', 'Male', 'Security', '18000'),
(00004, 'Khanittha Kongsangchai', '25', '0895937480', 'Female', 'IT Support', '19800'),
(00005, 'Janthana Tawisuwan', '20', '0905519610', 'Female', 'Cook', '25700'),
(00006, 'Aphichat Udomprecha', '23', '0908086710', 'Female', 'Security', '16000'),
(00007, 'Yaowapha Kitjakarn', '29', '0888346480', 'Male', 'IT Support', '28600'),
(00008, 'Ukrit Suttirat', '35', '0881469490', 'Male', 'Waiter', '18700'),
(00009, 'Rudee Udomprecha', '19', '0859041650', 'Female', 'Clerk', '25200'),
(00010, 'Sangwal Kongsangchai', '35', '0946288560', 'Female', 'Security', '25200');

CREATE TABLE orders(
	order_id 	INT(8) PRIMARY KEY,
	order_date	DATETIME,
	order_status ENUM('Registered','In-Progress','Completed'));

INSERT INTO orders
VALUE(00000001, '2018-4-21/12.51', 'Completed'),
(00000002, '2018-4-21/21.22', 'Completed'),
(00000003, '2018-4-22/10.33', 'Completed'),
(00000004, '2018-4-22/18.55', 'Completed'),
(00000005, '2018-4-23/07.18', 'In-Progress'),
(00000006, '2018-4-23/07.52', 'In-Progress'),
(00000007, '2018-4-23/08.02', 'In-Progress'),
(00000008, '2018-4-23/11.57', 'Registered');

CREATE TABLE order_item(
	item_qtn int(8),
    item_price float(8,2),
    item_id int(8) PRIMARY KEY);
    
INSERT INTO order_item
VALUE(00000007, '120.00', 00000001),
(00000015, '15.00', 00000002),
(00000002, '399', 00000003);

CREATE TABLE service(
	service_id int(5) PRIMARY KEY,
    service_type varchar(32) not null,
    service_price float(8,2) not null);
    
INSERT INTO service
VALUE(00001, 'spa', '500.00'),
(00002, 'gym','100.00');

CREATE TABLE reserve_data(
	pay_method varchar(255) not null,
    reserve_id INT(8) primary key,
    reserve_data varchar(255),
    data_status enum('Reserved','In-Room','CheckedOut','Cancelled') not null,
    checkin_date datetime,
    checkout_date datetime);
    
INSERT INTO reserve_data
VALUE('money tranfer', 00000001, '', 'In-Room', '25-4-2018', '30-4-2018'),
('money tranfer', 00000002, '', 'CheckedOut', '22-4-2018', '36-4-2018'),
('paypal', 00000003, 'Cancelled', '18-4-2018', '22-4-2018'),
('credit card', 00000004, 'Reserved', '4-5-2018', '15-5-2018');

CREATE TABLE room(
	room_id int(4) PRIMARY KEY,
    roon_name varchar(255) not null,
    building varchar(255) not null,
    floor int(3) not null);
    
INSERT INTO room
VALUE(0001, 'Suite', 'A', 008),
(0002, ' Villa','SP', 001),
(0003, ' Villa','SP', 001),
(0004, 'standard', 'C', 004),
(0005, 'standard', 'C', 003),
(0006, 'Suite', 'A', 007);

CREATE TABLE room_type(
	type_id int(5) primary key,
    type_description varchar(255),
    type_name varchar(64) not null,
    price float(8,2),
    type_image text);
    
INSERT INTO room_type
VALUE
(00010, '30sqm. room with single bed. Full facility. Maxinum 3 persons.', 'Standard Room - Single bed', 990.00,'Picture/Room/Std-Single1'),
(00011, '30sqm. room with twin bed. Full facility. Maxinum 3 persons.', 'Standard Room - Twin bed', 990.00,'Picture/Room/Std-Twin1'),
(00020, '34sqm. room with single bed. Full facility. Maxinum 3 persons.', 'Delux Room - Single bed', 1490.00,'Picture/Room/Dlx-Single1'),
(00021, '34sqm. room with twin bed. Full facility. Maxinum 3 persons.', 'Delux Room - Twin bed', 1590.00,'Picture/Room/Dlx-Twin1'),
(00040, '52sqm. room with double single bed. Full facility. Maxinum 7 persons.', 'VIP', 3490.00,'Picture/Room/VIP-1')
