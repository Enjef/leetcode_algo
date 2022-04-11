# Write your MySQL query statement below
-- 90.26%
SELECT employee_id, IF(employee_id%2 = 1 AND name NOT LIKE 'M%', salary, 0) as bonus
FROM Employees
ORDER BY employee_id

-- best
select employee_id , if(employee_id % 2 !=0 and name not like "M%",salary,0) as  bonus from employees;

-- 2nd best
select employee_id, (
    case
    when employee_id % 2 = 1 and name not like "M%" then salary
    else 0
    end
) as bonus
from Employees
order by employee_id
