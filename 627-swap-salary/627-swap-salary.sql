# Write your MySQL query statement below
UPDATE salary SET sex=CASE sex 
    When 'm' Then 'f'
    ELSE 'm'
    END;