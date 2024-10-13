# Write your MySQL query statement below

select name, bonus from (SELECT e.*,b.bonus from Employee e
left join Bonus b
on e.empId = b.empId) as b
where bonus is null or bonus < 1000