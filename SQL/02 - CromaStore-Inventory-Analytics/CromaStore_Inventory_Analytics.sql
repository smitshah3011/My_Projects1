/*
PROJET NAME: CromaStore Inventory Analytics
OBJECTIVE: To manage and analyze product inventory and manufacturer data for an electronics retail store.
TECHNIQUES USED: DDL (Data Definition Language), DML (Data Manipulation Language), SQL Joins, Subqueries, and Aggregate Functions.
*/

show databases;

create database croma_store;

use croma_store;

CREATE TABLE Manufacturers (
    Manufacturer_Code INT PRIMARY KEY,
    Manufacturer_Name VARCHAR(100)
);

CREATE TABLE Product_Inventory (
    Product_Code INT PRIMARY KEY,
    Product_Name VARCHAR(100),
    Product_Price INT,
    Manufacturer_Code INT,
    FOREIGN KEY (Manufacturer_Code) 
        REFERENCES Manufacturers(Manufacturer_Code)
);

INSERT INTO Manufacturers (Manufacturer_Code, Manufacturer_Name) VALUES
(1, 'Western Digital'),
(2, 'Samsung'),
(3, 'Hewlett Packard'),
(4, 'Corsair'),
(5, 'Asus'),
(6, 'Ant esports'),
(7, 'Cosmic Byte'),
(8, 'Zebronics'),
(9, 'TP-Link'),
(10, 'BoAt');

INSERT INTO Product_Inventory (Product_Code, Product_Name, Product_Price, Manufacturer_Code) VALUES
(1, '1 TB Hard Disk Drive', 2500, 1),
(2, 'Printer', 6500, 3),
(3, '64 GB Pen Drive', 700, 6),
(4, '6 GB Graphic Card', 12800, 5),
(5, '22 Inches Monitor', 10600, 2),
(6, '512 GB Solid State Drive', 4200, 1),
(7, 'Mouse', 400, 6),
(8, '450 Watt Power Supply Unit', 3600, 4),
(9, 'Printer Cartridge', 2500, 3),
(10, 'Membrane Keyboard', 900, 4),
(11, 'Bluetooth Speakers', 2000, 10),
(12, '42 Inches Television', 24600, 2),
(13, 'CPU Cabinet', 1900, 6),
(14, 'Laptop Adjustable Stand', 1250, 7),
(15, '8 GB RAM', 2600, 4),
(16, 'Motherboard', 6500, 8),
(17, 'Ergonomic Chair', 9700, 6),
(18, 'Monitor Arm Stand', 2600, 7),
(19, 'Wifi Adapter', 300, 9),
(20, 'HD Webcam', 1000, 8);

select * from Manufacturers;
select * from Product_Inventory;

-- 1 Select the names of all the products in the inventory.

select product_name from Product_Inventory;

-- 2 Select the names and the prices of all the products.

select product_name,product_price from Product_Inventory;

-- 3 Use an Alias "Name" and print all product names

select product_name as Product from Product_Inventory;

-- 4 Select the name of the products with a price less than or equal to 8000 Indian Rupees.

select product_name,product_price from Product_Inventory
where product_price <= 8000;

-- 5 Select all the products with a price between 2000 and 10000 Indian Rupees.

select product_name,product_price from Product_Inventory
where product_price between 2000 and 8000;

-- 6 List the details of all such products whose manufacturer_code is 6.

select * from Product_Inventory
where Manufacturer_code = 6;

-- 7 List the details of all such products whose manufacturer_code is 6 
-- 	 as well as their price is greater than 5000.

select * from Product_Inventory
where Manufacturer_code = 6 and product_price > 5000;

-- 8 List the details of all such products other than whose manufacturer_code is 6.

select * from Product_Inventory
where Manufacturer_code != 6;

-- 9 Select the name of the products whose name starts with 'M'.

select product_name from Product_Inventory
where product_name like "M%";

-- 10 List the name of products whose name starts with "M" and ends with "D".

select product_name from Product_Inventory
where product_name like "M%D";

-- 11 List the name of products which starts from "M" ends with "D" 
--    but also has ONLY 9 characters in between.

select product_name from Product_Inventory
where product_name like "M_________D";

-- 12 Concatenate name of the product with its price in a single column.

select concat(product_name, ":- ",product_price) as Product_Details from Product_Inventory;

-- 13 Select the name and price in dollars (i.e. the price must be divided by 80.)

select product_name,product_price,product_price/80 as Price_in_dollar from Product_Inventory;

-- 14 Compute the average price of all the products in Indian Rupees.

select avg(product_price) as Avg_price from Product_Inventory;

-- 15 Compute the average price of all products with manufacturer code equal to 3.

select avg(product_price) from Product_Inventory
where manufacturer_code = 3;

-- 16 What is the total cost of products where manufacturer_code is 2?

select sum(product_price) from product_inventory
where manufacturer_code = 2;

-- 17 Compute the number of products with a price greater than or equal to 5000.

select count(*) from product_inventory
where product_price >= 5000;

-- 18 Select the name and price of all products with a price larger than or equal to 5000 Indian 
-- Rupees and sort them by price (in descending order), and then by their name (in ascending order).

select product_name,product_price from product_inventory
where product_price >= 5000 
order by product_price desc,product_name asc;

-- 19 Select all the data from the inventory, including all the data for each product's manufacturer.

select * from product_inventory p 
join manufacturers m on p.manufacturer_code = m.manufacturer_code;

-- 20 Select the product name, price, and manufacturer name of all the products.

select p.product_name,p.product_price,m.Manufacturer_name from 
Product_Inventory p left join Manufacturers m
on p.manufacturer_code = m.manufacturer_code;

-- 21 Select the average price of each manufacturer's products, showing only the manufacturer's code.

select Manufacturer_code,avg(product_price) as avg_price from 
product_inventory 
group by Manufacturer_code;

-- 22 Select the average price of each manufacturer's products, showing the manufacturer's name.

select m.Manufacturer_name,avg(p.product_price) as avg_price from 
product_inventory p join Manufacturers m
on p.manufacturer_code = m.manufacturer_code
group by m.Manufacturer_name;

-- 23 Select the names of manufacturer whose products have an average price greater than or equal to 5000 Indian Rupees.

select m.Manufacturer_name,avg(p.product_price) as avg_price from Manufacturers as m join Product_Inventory as p
on m.Manufacturer_code = p.Manufacturer_code
group by m.Manufacturer_name
having avg_price >= 5000;

-- 24 Select the name and price of the cheapest product.

-- 1st way
select min(product_price) from product_inventory;
select product_name,product_price from product_inventory
where product_price = (select min(product_price) from product_inventory);

-- 2nd way
select product_name,product_price from product_inventory
order by product_price limit 1; 

-- 25 Select the name of each manufacturer along with the name and price of its 
--    most expensive product. 

select m.Manufacturer_name,max(product_price) from 
Product_Inventory p join Manufacturers m
on m.Manufacturer_code = p.Manufacturer_code
group by m.Manufacturer_name;

SELECT m.Manufacturer_Name, p.Product_Name, p.Product_Price
FROM Product_Inventory p
JOIN Manufacturers m
ON p.Manufacturer_Code = m.Manufacturer_Code
WHERE p.Product_Price = (
    SELECT MAX(Product_Price)
    FROM Product_Inventory
    WHERE Manufacturer_Code = p.Manufacturer_Code
);

-- 26 Add a new product: Speaker with a price 1000 INR and manufacturer code 10.

insert into Product_Inventory values
(21,"Speaker",1000,10);
select * from Product_Inventory;

-- 27 Update the name of the product "Speakers" to "Wired Speakers". 

update Product_Inventory set product_name = "Wired Speakers"
where product_name = "Speaker";
select * from Product_Inventory;

-- 28 Apply a 10% discount to all products. 

select *,product_price-product_price*0.1 from Product_Inventory

-- other way

UPDATE Product_Inventory
SET Product_Price = Product_Price * 0.9;

-- 29 Apply a 10% discount to all products with a price greater than or equal to 5000 Indian Rupees.

select *,product_price-product_price*0.1 from Product_Inventory
where product_price >= 5000;

-- 30 List the name of the products along with their manufacturer name and price and arrange them as per their price.

select product_name,manufacturer_name,product_price from
Product_Inventory join Manufacturers
on Manufacturers.Manufacturer_code = Product_Inventory.Manufacturer_code
order by product_price;




select * from Manufacturers;
select * from Product_Inventory;

25