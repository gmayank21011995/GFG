
-- dept wise 2nd highest salary
with tmp as(
  select t.*, dense_rank() over (partition by dept order by sal desc)as r from emp t)
select * from tmp where r = 2

-- 2nd highest salary
with tmp as(
  select t.*, dense_rank() over (order by sal desc) as r from emp t)
  select * from tmp where r = 2

-- find duplicate records
with tmp as(
  select t.*, count(*) over (partition by name, dept)as r from emp t)
  select * from tmp where r > 1
  
-- cumulative sum dept wise
with tmp as(
select t.*, sum(salary) over (partition by dept order by id asc) as cum_sum from emp t)
select * from tmp

-- Top N salaries per department (e.g., top 2)
with tmp as(
select *, dense_rank() over (partition by dept order by sal desc) r from emp)
select * from tmp where r <= n

-- Find employees who earn more than department average
with tmp as(
select *, avg(sal) over (partition by dept) as dept_avg from emp e)
select * from tmp where sal > dept_avg

-- Find consecutive login dates (gap of 1 day)
with LoginDiffs as(
select user_id, login_date, LAG(login_date) over (partition by user_id order by login_date)
as prev_login from emp)
select
    user_id,
    prev_login_date,
    login_date
from
    LoginDiffs
where
    -- Database-specific date arithmetic for 1-day difference
    -- SQL Server: DATEDIFF(day, prev_login_date, login_date) = 1
    -- MySQL: DATEDIFF(login_date, prev_login_date) = 1
    -- PostgreSQL: login_date = prev_login_date + INTERVAL '1 day'
    -- Oracle: login_date = prev_login_date + 1 (for DATE types)
    -- Or for generic: ABS(login_date - prev_login_date) = 1 (if the difference is in days directly)
    -- Let's use a common date diff function and assume it returns days
    DATEDIFF(day, prev_login_date, login_date) = 1
ORDER BY
    user_id, login_date;

-- Find first and last salary for each employee
with tmp as(
select *, 
row_number() over (partition by emp_id order by credited_date asc) as asc_rnk,
row_number() over (partition by emp_id order by credited_date desc) as desc_rnk
from emp)

select * from 
tmp left_id
join 
tmp right_id on left_id.emp_id = right_id.emp_id 
where left_id.asc_rnk = 1 and right_id.desc_rnk = 1

-- Show how many employees joined before each employee
select e1.emp_id, count(e2.emp_id) from emp e1
left join emp e2
on e2.hire_dt < e1.hire_dt
group by e1.emp_id, e1.hire_dt
order by e1.emp_id, e1.hire_dt asc

--  Find time difference between two events
with EventDiffs as (
    select
        id,
        event_time,
        LAG(event_time, 1, NULL) OVER (PARTITION BY id ORDER BY event_time ASC) as prev_event_time
    from
        event_log
)
select
    id,
    event_time,
    prev_event_time,
    -- Database-specific calculation for time difference:
    -- SQL Server: DATEDIFF(second, prev_event_time, event_time) AS time_diff_seconds
    -- MySQL: TIMESTAMPDIFF(SECOND, prev_event_time, event_time) AS time_diff_seconds
    -- PostgreSQL: EXTRACT(EPOCH FROM (event_time - prev_event_time)) AS time_diff_seconds
    -- Oracle: (event_time - prev_event_time) * 24 * 60 * 60 (if DATE) or EXTRACT(SECOND FROM (event_time - prev_event_time)) + ... (if TIMESTAMP)
    -- Example for SQL Server:
    DATEDIFF(second, prev_event_time, event_time) AS time_diff_seconds
from
    EventDiffs
ORDER BY
    id, event_time;

-- find the last person to enter a bus such that the total accumulated weight does not exceed 1000 kg, and people enter in a defined sequence, you can use a running total (cumulative sum) in SQL.
WITH running_weight AS (
    SELECT 
        person_id,
        name,
        weight,
        seq,
        SUM(weight) OVER (ORDER BY seq) AS total_weight
    FROM passengers
)
SELECT 
    person_id,
    name,
    weight,
    seq,
    total_weight
FROM running_weight
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
