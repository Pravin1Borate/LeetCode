/* Write your T-SQL query statement below */

select a.unique_id,b.name
from Employees b left join
EmployeeUNI a on b.id = a.id