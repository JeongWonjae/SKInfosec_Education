
INSERT INTO car_menu VALUES('CAR0001','KIA K5','BLACK','NEW','123456789','2020','10000');
INSERT INTO car_menu VALUES('CAR0002','KIA K3','RED','OLD','123456790','2019','20000');
INSERT INTO car_menu VALUES('CAR0003','BMW 1000','PINK','NEW','123456791','2020','40000');
INSERT INTO car_menu VALUES('CAR0004','Benz A-Class','BLACK','NEW','123456792','2020','40000');
INSERT INTO car_menu VALUES('CAR0005','Sonata','PINK','OLD','123456793','2018','40000');
INSERT INTO car_menu VALUES('CAR0006','LAMBORGHNI URS','YELLOW','NEW','123456794','2020','10000');
INSERT INTO car_menu VALUES('CAR0007','BUGATTI','GREEN','OLD','123456795','2018','15000');
INSERT INTO car_menu VALUES('CAR0008','FERRARI 488','RED','NEW','123456796','2020','50000');
INSERT INTO car_menu VALUES('CAR0009','PORSHEE 911','BLUE','NEW','123456797','2020','35000');
INSERT INTO car_menu VALUES('CAR0010','TESAL MODEL S','WHITE','OLD','123456798','2019','40000');

INSERT INTO customer VALUES('C0001','Kim Suk-Ju','010-1111-1111','Gwangju');
INSERT INTO customer VALUES('C0002','Choi Youn-Young','010-2222-2222','Daegu');
INSERT INTO customer VALUES('C0003','Jeong Wonjae-Jae','010-3333-3333','Seoul');
INSERT INTO customer VALUES('C0004','Lee Do-Won','010-4444-4444','Seoul');
INSERT INTO customer VALUES('C0005','Taylor Swift','010-5555-5555','Geounggido');
INSERT INTO customer VALUES('C0006','Jo You-bin','010-6666-6666','Seoul');
INSERT INTO customer VALUES('C0007','LEE Young-Hwan','010-7777-7676','Seoul');
INSERT INTO customer VALUES('C0008','Bill Gates','010-8888-8888','Jeju');

INSERT INTO salesperson VALUES('S0001','Kelly','010-9874-2548','kelly@abc.net');
INSERT INTO salesperson VALUES('S0002','Jack','010-1459-1483','jack@abc.net');
INSERT INTO salesperson VALUES('S0003','Hulk','010-8157-2168','hulk@abc.net');
INSERT INTO salesperson VALUES('S0004','Ironman','010-9888-7888','ironman@aaa.com');
INSERT INTO salesperson VALUES('S0005','Tor','010-4455-5566','tor@aaa.com');
INSERT INTO salesperson VALUES('S0006','Maple','010-6972-4495','maple@nexon.com');

INSERT INTO order_details VALUES('O0001','C0001','','CAR0001','10000');
insert into sales_invoice values('I0001','C0001','S0001','O0001');

INSERT INTO mechanic VALUES('M0001','010-1234-2222','alice@repairB.com','Alice','A','Mon Tue Wen Fri');
INSERT INTO mechanic VALUES('M0002','010-1112-5828','mike@repairA.net','Mike','A','Wen Fri');
INSERT INTO mechanic VALUES('M0003','010-1548-7326','jack@repairA.net','Jack','B','Mon Wen Fri');
INSERT INTO mechanic VALUES('M0004','010-5876-5885','tom@repairB.net','Tom','B','Sat Sun');
INSERT INTO mechanic VALUES('M0005','010-2468-2489','jodeon@repairA.net','Jodeon','B','Mon Tue Thr');
INSERT INTO mechanic VALUES('M0006','010-4889-5792','trump@repairA.net','Trump','B','Wen Fri Sat Sun');

INSERT INTO service_menu VALUES('SV0001','Clean','10000','N');
INSERT INTO service_menu VALUES('SV0002','Change','20000','Y');
INSERT INTO service_menu VALUES('SV0003','Repair','30000','N');

INSERT INTO product_menu VALUES('PA0001','Silver Tire','100');
INSERT INTO product_menu VALUES('PA0002','Black Tire','200');
INSERT INTO product_menu VALUES('PA0003','Red Tire','300');
INSERT INTO product_menu VALUES('PA0004','Wood Handle','100');
INSERT INTO product_menu VALUES('PA0005','Steel Handle','200');

INSERT INTO product VALUES('P0001','PA0001','SV0002','Tire');
INSERT INTO product VALUES('P0002','PA0002','SV0002','Tire');
INSERT INTO product VALUES('P0003','PA0003','SV0002','Tire');
INSERT INTO product VALUES('P0004','PA0004','SV0002','Handle');
INSERT INTO product VALUES('P0005','PA0005','SV0002','Handle');