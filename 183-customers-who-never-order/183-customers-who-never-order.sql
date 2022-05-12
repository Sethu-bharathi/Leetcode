# Write your MySQL query statement below
SELECT name as Customers FROM customers  where id NOT in (select customerid from orders)
