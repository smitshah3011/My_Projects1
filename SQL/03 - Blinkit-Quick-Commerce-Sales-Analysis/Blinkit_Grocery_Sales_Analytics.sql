/*
PROJECT NAME: Blinkit Grocery Sales Analysis
OBJECTIVE: To analyze sales performance, item visibility, and outlet patterns for a quick-commerce platform.
TECHNIQUES USED: Data Aggregation, Filtering (WHERE), Sorting (ORDER BY), Grouping (GROUP BY), and Table Aliasing.
*/

show databases;

create database Blinkit;

use Blinkit;

show tables;

select * from 1759924698862_grocery_store;

alter table 1759924698862_grocery_store
rename to Blinkit_store;

select * from Blinkit_store;

-- 1 Import Data from table Grocery Sales using the provided CSV File.

select * from Blinkit_store;

-- 2 Write an SQL query to show all Item_Identifier

select Item_Identifier from Blinkit_store;

-- 3 Write an SQL query to show count of total Item_Identifier.

select count(Item_Identifier) from Blinkit_store;

-- 4 Write an SQL query to show maximum Item Weight.

select max(Item_Weight) from Blinkit_store;

-- 5 Write an SQL query to show minimum Item Weight.

select min(Item_Weight) from Blinkit_store;

-- 6 Write an SQL query to show average Item_Weight.

select avg(Item_Weight) from Blinkit_store;

-- 7 Write an SQL query to show count of Item_Fat_Content WHERE Item_Fat_Content is Low Fat.

select count(Item_Fat_Content) from Blinkit_store
where Item_Fat_Content = "Low Fat";

-- 8 Write an SQL query to show count of Item_Fat_Content WHERE Item_Fat_Content is Regular.

select count(Item_Fat_Content) from Blinkit_store
where Item_Fat_Content = "Regular";

-- 9 Write an SQL query to show maximum Item_MRP 

select max(Item_MRP) from Blinkit_store;

-- 10 Write an SQL query to show minimum Item_MRP

select min(Item_MRP) from Blinkit_store;

-- 11 Write an SQL query to show Item_Identifier , Item_Fat_Content ,Item_Type, 
--    Item_MRP whose Item_MRP is greater than 200.

select Item_Identifier , Item_Fat_Content ,Item_Type, Item_MRP from Blinkit_store
where Item_MRP > 200;

-- 12 Write an SQL query to show maximum Item_MRP WHERE Item_Fat_Content is Low Fat 

select max(Item_MRP) from Blinkit_store
where Item_Fat_Content = "Low Fat";

-- 13 Write an SQL query to show minimum Item_MRP whose Item_Fat_Content is Low Fat 

select min(Item_MRP) from Blinkit_store
where Item_Fat_Content = "Low Fat";

-- 14 Write an SQL query to show ALL DATA WHERE item MRP is BETWEEN 50 to 100

select * from Blinkit_store
where Item_MRP between 50 and 100;

-- 15 Write an SQL query to show ALL UNIQUE value of Item_Fat_Content

select distinct(Item_Fat_Content) from Blinkit_store;

-- 16 Write an SQL query to show ALL UNIQUE value of  Item_Type 

select distinct(Item_Type) from Blinkit_store;

-- 17 Write an SQL query to show ALL DATA in descending ORDER by Item MRP 

select * from Blinkit_store
order by Item_MRP desc;

-- 18 Write an SQL query to show ALL DATA in ascending ORDER by Item_Outlet_Sales

select * from Blinkit_store
order by Item_Outlet_Sales asc;

-- 19 Write an SQL query to show ALL DATA in ascending by Item_Type

select * from Blinkit_store
order by Item_Type;

-- 20 Write an SQL query to show DATA of item_type dairy & Meat

select * from Blinkit_store
where item_type in ("dairy","Meat")

-- 21 Write an SQL query to show ALL UNIQUE value of Outlet_Size 

select distinct(Outlet_Size) from Blinkit_store;

-- 22 Write an SQL query to show ALL UNIQUE value of Outlet_Location_Type

select distinct(Outlet_Location_Type) from Blinkit_store;

-- 23 Write an SQL query to show ALL UNIQUE value of Outlet_Type 

select distinct(Outlet_Type) from Blinkit_store;

-- 24 Write an SQL query to show count of number of items by Item_Type  and order it in descending order

select Item_Type,count(Item_Type) as number_of_items from  Blinkit_store
group by Item_Type
order by number_of_items desc;

-- 25 Write an SQL query to show count of number of items by Outlet_Size and ordered it in ascending order 

select Outlet_Size,count(Outlet_Size) as number_of_Outlet_Size from  Blinkit_store
group by Outlet_Size
order by number_of_Outlet_Size;

-- 26 Write an SQL query to show count of number of items by Outlet_Type  and ordered it in descending order.

select Outlet_Type,count(Outlet_Type) as number_of_Outlet_Type from  Blinkit_store
group by Outlet_Type
order by number_of_Outlet_Type desc;

-- 27 Write an SQL query to show count of items by Outlet_Location_Type and order it indescending order

select Outlet_Location_Type,count(Outlet_Type) as number_of_Outlet_Location_Type from  Blinkit_store
group by Outlet_Location_Type
order by number_of_Outlet_Location_Type;

-- 28 Write an SQL query to show maximum MRP by Item_Type 

select Item_Type,max(Item_mrp) from Blinkit_store
group by Item_Type;

-- 29 Write an SQL query to show minimum MRP by Item_Type 

select Item_Type,min(Item_mrp) from Blinkit_store
group by Item_Type;

-- 30 Write an SQL query to show minimum MRP by Outlet_Establishment_Year and order it in descending order.

select Outlet_Establishment_Year,min(Item_mrp) from Blinkit_store
group by Outlet_Establishment_Year
order by min(Item_mrp) desc;

-- 31 Write an SQL query to show maximum MRP by Outlet_Establishment_Year and order it in descending order.

select Outlet_Establishment_Year,max(Item_mrp) from Blinkit_store
group by Outlet_Establishment_Year
order by max(Item_mrp) desc;

-- 32 Write an SQL query to show average MRP by Outlet_Size and order it in descending order.

select Outlet_Size,avg(Item_mrp) from Blinkit_store
group by Outlet_Size
order by avg(Item_mrp) desc;

-- 33 Write an SQL query to Average MRP by Outlet_Type and ordered in ascending order.

select Outlet_Type,avg(Item_mrp) from Blinkit_store
group by Outlet_Type
order by avg(Item_mrp);

-- 34 Write an SQL query to show maximum MRP by Outlet_Type

select Outlet_Type,max(Item_mrp) from Blinkit_store
group by Outlet_Type;

-- 35 Write an SQL query to show maximum Item_Weight by Item_Type 

select Item_Type,max(Item_Weight) from Blinkit_store
group by Item_Type;

-- 36 Write an SQL query to show maximum Item_Weight by Outlet_Establishment_Year 

select Outlet_Establishment_Year,max(Item_Weight) from Blinkit_store
group by Outlet_Establishment_Year;

-- 37 Write an SQL query to show minimum Item_Weight by Outlet_Type 

select Outlet_Type,min(Item_Weight) from Blinkit_store
group by Outlet_Type;

-- 38 Write an SQL query to show average Item_Weight by Outlet_Location_Type and arrange it by descending order

select Outlet_Location_Type,avg(Item_Weight) from Blinkit_store
group by Outlet_Location_Type
order by avg(Item_Weight) desc;

-- 39 Write an SQL query to show maximum Item_Outlet_Sales by Item_Type

select Item_Type,max(Item_Outlet_Sales) from Blinkit_store
group by Item_Type;

-- 40 Write an SQL query to show minimum Item_Outlet_Sales by Item_Type 

select Item_Type,min(Item_Outlet_Sales) from Blinkit_store
group by Item_Type;

-- 41 Write an SQL query to show minimum Item_Outlet_Sales by Outlet_Establishment_Year 

select Outlet_Establishment_Year,min(Item_Outlet_Sales) from Blinkit_store
group by Outlet_Establishment_Year;

-- 42 Write an SQL query to show maximum Item_Outlet_Sales by Outlet_Establishment_Year and order it by descending order

select Outlet_Establishment_Year,max(Item_Outlet_Sales) from Blinkit_store
group by Outlet_Establishment_Year
order by Outlet_Establishment_Year desc;

-- 43 Write an SQL query to show average Item_Outlet_Sales by Outlet_Size and order it it descending order

select Outlet_Size,avg(Item_Outlet_Sales) from Blinkit_store
group by Outlet_Size
order by Outlet_Size desc;

-- 44 Write an SQL query to show average Item_Outlet_Sales by Outlet_Type

select Outlet_Type,avg(Item_Outlet_Sales) from Blinkit_store
group by Outlet_Type;

-- 45 Write an SQL query to show maximum Item_Outlet_Sales by Outlet_Type 

select Outlet_Type,min(Item_Outlet_Sales) from Blinkit_store
group by Outlet_Type;

-- 46 Write an SQL query to show total Item_Outlet_Sales by Item_Type 

select Item_Type,sum(Item_Outlet_Sales) from Blinkit_store
group by Item_Type;

-- 47 Write an SQL query to show total Item_Outlet_Sales by Item_Fat_Content 

select Item_Fat_Content,sum(Item_Outlet_Sales) from Blinkit_store
group by Item_Fat_Content;

-- 48 Write an SQL query to show maximum Item_Visibility by Item_Type

select Item_Type,max(Item_Visibility) from Blinkit_store
group by Item_Type;

-- 49 Write an SQL query to show Minimum Item_Visibility by Item_Type 

select Item_Type,min(Item_Visibility) from Blinkit_store
group by Item_Type;

-- 50 Write an SQL query to show total Item_Outlet_Sales by Item_Type but only WHERE Outlet_Location_Type is Tier 1 

select Item_Type,sum(Item_Outlet_Sales) from Blinkit_store
where Outlet_Location_Type = "Tier 1"
group by Item_Type;

-- 51 Write an SQL query to show total Item_Outlet_Sales by Item_Type WHERE Item_Fat_Content is ONLY Low Fat & LF

select Item_Type,sum(Item_Outlet_Sales) from Blinkit_store
where Item_Fat_Content in ("Low Fat","LF")
group by Item_Type;



select * from Blinkit_store;