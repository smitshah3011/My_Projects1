-- show databases;

-- create database pranav_uber;
-- 
-- show databases;
-- 
 use pranav_uber;


-- =============================================================
-- PROJECT: Uber Data Analysis Case Study
-- TOTAL QUESTIONS: 50
-- TOOLS USED: MySQL 
-- =============================================================

select * from drivers;
select * from passangers;
select * from rides;


-- -------------------------------------------------------------
-- PART 1: BASIC LEVEL QUESTIONS (1-20)
-- Focus: SELECT, WHERE, GROUP BY, ORDER BY, Aggregates
-- -------------------------------------------------------------

-- 1. What are & how many unique pickup locations are there in the dataset?

select distinct(pickup_location) from rides;

select count(pickup_location) from rides;

select distinct(pickup_location),count(pickup_location) from rides
group by pickup_location;

-- 2. What is the total number of rides in the dataset?

select count(ride_id) from rides;

-- 3. Calculate the average ride duration.

select round(avg(ride_duration),2) from rides;

-- 4. List the top 5 drivers based on their total earnings.

select * from drivers
order by earnings desc limit 5;

-- other way
select driver_id, sum(earnings) from  drivers
group by driver_id
order by sum(earnings) desc
limit 5;

WITH top_drivers AS (
    SELECT driver_id, SUM(earnings) AS total_earnings
    FROM drivers
    GROUP BY driver_id
    ORDER BY total_earnings DESC
    LIMIT 5
)
SELECT d.*, t.total_earnings
FROM drivers d
JOIN top_drivers t ON d.driver_id = t.driver_id;

-- 5. Calculate the total number of rides for each payment method.

select payment_method,count(ride_id) as no_of_rides from rides
group by payment_method;

select payment_method, count(*) No_of_Rides from rides
group by payment_method;

-- 6. Retrieve rides with a fare amount greater than 20.

select * from rides
where fare_amount >= 20;

-- 7. Identify the most common pickup location.

select pickup_location,count(pickup_location) as no_of_pickup_location from rides
group by pickup_location
order by no_of_pickup_location desc
limit 1;

select pickup_location, count(*) from rides
group by pickup_location
order by count(*) desc
limit 1;

-- 8. Calculate the average fare amount.

select avg(fare_amount) from rides;

-- 9. List the top 10 drivers with the highest average ratings.

select * from drivers
order by rating desc
limit 10;

-- other way
select driver_name, avg(rating) from drivers
group by driver_name
order by avg(rating) desc
limit 10;

select driver_id, driver_name, avg(rating) from drivers
group by driver_id, driver_name
order by avg(rating) desc
limit 10

SELECT d.driver_id, d.driver_name, t.avg_rating
FROM drivers d
JOIN (
    SELECT driver_id, AVG(rating) AS avg_rating
    FROM drivers
    GROUP BY driver_id
    ORDER BY avg_rating DESC
    LIMIT 10
) AS t
ON d.driver_id = t.driver_id
ORDER BY t.avg_rating DESC;

-- 10. Calculate the total earnings for all drivers.

select sum(earnings) from drivers;

-- 11. How many rides were paid using the "Cash" payment method?

select payment_method,count(*) from rides
where payment_method = "cash";

-- 12. Calculate the number of rides & average ride distance for rides originating from the 'Dhanbad' pickup location.

select count(*),avg(ride_distance),pickup_location from rides
where pickup_location = "Dhanbad";


-- 13. Retrieve rides with a ride duration less than 10 minutes.

select * from rides
where ride_duration < 10;

#14. List the passengers who have taken the most number of rides.

select r.passenger_id,p.passenger_name,count(r.passenger_id) as total_ride from
passangers as p join rides as r
on p.passenger_id = r.passenger_id
group by passenger_name,passenger_id
order by total_ride desc
limit 1;

-- other way
select passenger_id, count(*) from rides 
group by passenger_id
order by count(*) desc
limit 1;

select passangers.passenger_id Passenger_id,
       passangers.passenger_name Passanger_name,
       count(rides.ride_id)
from rides
inner join passangers
on passangers.passenger_id = rides.passenger_id
group by passangers.passenger_id, passangers.passenger_name
order by count(rides.ride_id) desc
limit 1; 

-- 15. Calculate the total number of rides for each driver in descending order.

select d.driver_id driver_id,d.driver_name driver_name,count(r.driver_id) total_ride from 
drivers d inner join rides r
on d.driver_id = r.driver_id
group by d.driver_id,d.driver_name
order by total_ride desc;

-- other way
select driver_id, count(*) from rides
group by driver_id 
order by count(*) desc;

select drivers.driver_id, drivers.driver_name, count(rides.ride_id)
from drivers
inner join rides
on drivers.driver_id = rides.driver_id
group by drivers.driver_id,drivers.driver_name 
order by count(rides.ride_id) desc;

-- 16. Identify the payment methods used by passengers who took rides from the 'Gandhinagar' pickup location.

select distinct(payment_method) from rides
where pickup_location = "Gandhinagar";

-- 17. Calculate the average fare amount for rides with a ride distance greater than 10.

select avg(fare_amount) from rides
where ride_distance > 10;

-- 18. List the drivers in descending order accordinh to their total number of rides.

select driver_id,driver_name, total_rides from drivers
order by total_rides desc;

-- 19. Calculate the percentage distribution of rides for each pickup location.

select distinct(pickup_location),count(ride_id) as total_ride,sum(*)/tottal_ride from rides
group by pickup_location;

select count(ride_id) from rides;
select 14300/(select count(ride_id) from rides) from rides;
select count(ride_id)/(select count(ride_id) from rides) from rides;

select pickup_location,count(ride_id),(count(ride_id)*100)/(select count(ride_id) from rides) from rides
group by pickup_location;

-- group by pickup_location
-- 20. Retrieve rides where both pickup and dropoff locations are the same.

select * from rides
where pickup_location = dropoff_location;

-- -------------------------------------------------------------
-- PART 2: INTERMEDIATE LEVEL QUESTIONS (21-40)
-- Focus: Joins, Having Clause, Date Functions, Subqueries
-- -------------------------------------------------------------

-- 21. List the passengers who have taken rides from at least 300 different pickup locations.

select passenger_id,count(distinct(pickup_location)) from rides
group by passenger_id
having count(distinct(pickup_location)) >= 300;

select passangers.passenger_id Passenger_id,
       passangers.passenger_name Passengers,
       count(distinct pickup_location) Distinct_Location
from passangers inner join rides
on passangers.passenger_id = rides.passenger_id
group by passangers.passenger_id, passangers.passenger_name
having count(distinct pickup_location)>=300;

-- 22. Calculate the average fare amount for rides taken on weekdays.

select avg(fare_amount) from rides
where DAYNAME(ride_timestamp) not in ("Saturday","Sunday");

-- other long way

select avg(fare_amount) 
from rides 
where dayofweek(str_to_date(ride_timestamp, '%m/%d/%y %H:%i'))>5;

select date_format("2022-11-08", "%M %D %Y");
select date_format("2022-11-08", "%W %M %e %Y");

select ride_timestamp,
       dayname(ride_timestamp),
       dayofweek(ride_timestamp)
from rides
where dayofweek(ride_timestamp) not in (1,7);

select avg(fare_amount) from rides 
where dayofweek(ride_timestamp) not in (1,7);#Sunday=1, Saturday=7

select avg(fare_amount) from rides 
where weekday(ride_timestamp) not in (6,5);#Monday=0, Sunday=6, Saturday=5

#23. Identify the drivers who have taken rides with distances greater than 19.

select driver_id,ride_distance from rides
where ride_distance > 19;

select d.driver_id,d.driver_name,r.ride_distance from
rides r inner join drivers d
on d.driver_id = r.driver_id
where r.ride_distance > 19;

-- 24. Calculate the total earnings for drivers who have completed more than 100 rides.

select driver_id,driver_name,earnings from drivers
where total_rides > 100;

select driver_id,driver_name,sum(earnings) from drivers
where total_rides > 100
group by driver_id,driver_name;

select driver_id, sum(earnings)
from drivers 
where driver_id in (
    select driver_id from rides
    group by driver_id
    having count(*) > 100   
)
group by driver_id; 

-- 25. Retrieve rides where the fare amount is less than the average fare amount.

select * from rides
where fare_amount < (select avg(fare_amount) from rides);

-- 26. Calculate the average rating of drivers who have driven rides with both 'Credit Card' and 'Cash' payment methods.

select d.driver_id,d.driver_name,avg(d.rating) from 
rides r join drivers d
on d.driver_id = r.driver_id
group by d.driver_id,d.driver_name;
having r.COUNT(DISTINCT payment_method) = 2;

SELECT 
    AVG(d.rating) AS avg_rating
FROM 
    drivers d
WHERE 
    d.driver_id IN (
        SELECT 
            driver_id
        FROM 
            rides
        WHERE 
            payment_method IN ('Cash', 'Credit Card')
        GROUP BY 
            driver_id
        HAVING 
            COUNT(DISTINCT payment_method) = 2
    );

-- 26. Calculate the average rating of drivers who have driven rides with both 'Credit Card' and 'Cash' payment methods.

select * from drivers;
select * from rides;

select avg(d.rating) from
drivers d inner join rides r
on d.driver_id = r.driver_id
where payment_method in ("Cash","Credit Card")
group by d.driver_id;

#27. List the top 3 passengers with the highest total spending.

select * from passangers
order by total_spent desc
limit 3;

#28. Calculate the average fare amount for rides taken during different months of the year.

select year(ride_timestamp),month(ride_timestamp),avg(fare_amount) from rides
group by month(ride_timestamp),year(ride_timestamp);

-- other way

select month(ride_timestamp) Months ,
       monthname(ride_timestamp) Month_Name,
       round(avg(fare_amount),2) AVG_Fareamount 
from rides
group by month(ride_timestamp), monthname(ride_timestamp)
order by month(ride_timestamp);

-- 29. Identify the most common pair of pickup and dropoff locations.

select pickup_location,dropoff_location,count(*) from rides
group by pickup_location,dropoff_location
order by count(*) desc;

-- 30. Calculate the total earnings for each driver and order them by earnings in descending order.

select driver_name,earnings from drivers
order by earnings desc;

-- other way

select driver_name, sum(earnings) from drivers
group by driver_name
order by sum(earnings) desc;

-- prac
select driver_name,count(driver_name),sum(earnings) from drivers
group by driver_name
order by count(driver_name) desc;

-- 31. List the passengers who have taken rides on their signup date.

select p.passenger_id,p.passenger_name,r.ride_id,p.signup_date,r.ride_timestamp from 
passangers p inner join rides r
on p.passenger_id = r.passenger_id
where p.signup_date = r.ride_timestamp;

-- 32. Calculate the average earnings for each driver and order them by earnings in descending order.

select driver_name,avg(earnings) from drivers
group by driver_name
order by avg(earnings) desc;

-- 33. Retrieve rides with distances less than the average ride distance.

select ride_id,ride_distance from rides
where ride_distance < (select avg(ride_distance) from rides);

-- 34. List the drivers who have completed the least number of rides.

select driver_name,total_rides from drivers
where total_rides = (select min(total_rides) from drivers)

-- 35. Calculate the average fare amount for rides taken by passengers who have taken at least 20 rides.

select p.passenger_id,p.passenger_name,p.total_rides,avg(fare_amount) from 
passangers p join rides r
on p.passenger_id = r.passenger_id
where total_rides >= 20
group by p.passenger_id,p.passenger_name,p.total_rides;

-- 36. Identify the pickup location with the highest average fare amount.

select pickup_location,avg(fare_amount) from rides
group by pickup_location
order by avg(fare_amount) desc
limit 1;

-- 37. Calculate the average rating of drivers who completed at least 100 rides.

select driver_name,avg(rating) from drivers
where total_rides >= 100
group by driver_name;

-- 38. List the passengers who have taken rides from at least 5 different pickup locations.

select passenger_id,count(distinct (pickup_location)) from rides
group by passenger_id
having count(distinct (pickup_location)) >= 5;

-- 39. Calculate the average fare amount for rides taken by passengers with ratings above 4.

select p.passenger_id,p.passenger_name,avg(r.fare_amount),p.rating from
passangers p inner join rides r
on p.passenger_id = r.passenger_id
where p.rating > 4
group by p.passenger_id,p.passenger_name,p.rating;

-- -------------------------------------------------------------
-- PART 3: ADVANCED LEVEL QUESTIONS (41-50)
-- Focus: Complex Subqueries, CTEs, Percentage Calculations
-- -------------------------------------------------------------

-- 40. Retrieve rides with the shortest ride duration in each pickup location.

select pickup_location,min(ride_duration) from rides
group by pickup_location
order by min(ride_duration) asc;
 
-- 41 List the drivers who have driven rides in all pickup locations.

select driver_id,count(distinct(pickup_location)) from rides
group by driver_id
having count(distinct(pickup_location)) = (select count(distinct(pickup_location)) from rides);

-- 42 Calculate the average fare amount for rides taken by passengers who have spent more than 300 in total.

select passenger_name,total_spent,avg(fare_amount) from passangers p join rides r
on p.passenger_id = r.passenger_id
where total_spent > 300
group by passenger_name,total_spent;

-- 43 List the bottom 5 drivers based on their average earnings.

select driver_name,avg(earnings) from drivers
group by driver_name
order by avg(earnings) asc 
limit 5;

-- 44 Calculate the sum fare amount for rides taken by passengers who have taken rides in different payment methods.

select sum(fare_amount) from rides 
where passenger_id in (
	select passenger_id from rides
	where payment_method in ("cash","credit card")
	group by passenger_id
	having count(distinct payment_method) = 2
)

-- 45 Retrieve rides where the fare amount is significantly above the average fare amount.

select * from rides
where fare_amount > (select avg(fare_amount) from rides);

-- 46 List the drivers who have completed rides on the same day they joined.

select * from drivers d join rides r on d.driver_id = r.driver_id
where join_date = ride_timestamp;

-- 47 Calculate the average fare amount for rides taken by passengers who have taken rides in different payment methods.

select avg(fare_amount) from rides 
where passenger_id in (
	select passenger_id from rides
	where payment_method in ("cash","credit card")
	group by passenger_id
	having count(distinct payment_method) = 2
)

-- 48 Identify the pickup location with the highest percentage increase in average fare amount compared to the overall average fare.

SELECT pickup_location,
       ((AVG(fare_amount) - (SELECT AVG(fare_amount) FROM rides)) 
        / (SELECT AVG(fare_amount) FROM rides)) * 100 AS pct_increase
FROM rides
GROUP BY pickup_location
ORDER BY pct_increase DESC
LIMIT 1;

-- 49 Retrieve rides where the dropoff location is the same as the pickup location.

select * from rides
where pickup_location = dropoff_location;

-- 50 Calculate the average rating of drivers who have driven rides with varying pickup locations.

select avg(rating) from drivers 
where driver_id in (select driver_id from rides
group by driver_id 
having count(distinct pickup_location) > 1);
