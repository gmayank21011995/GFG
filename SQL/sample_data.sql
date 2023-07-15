create table emp1
(
    empid1 varchar(10),
    emp_sal1 varchar(10)
)

create table emp2
(
    empid2 varchar(10),
    emp_sal2 varchar(10)
)

insert into emp1
values
("1","1000"),
("2","2000"),
("2","2000"),
("2","2000"),
("3","3000"),
(null,null),
(null,null)
(null,null)

insert into emp2
values
("1","1000"),
("2","2000"),
("2","2000"),
("3","3000"),
("3","3000"),
(null,null)

-- emp1 to emp2
-- inner join 10
-- left join 13
-- right join 11
-- full outer join 14
-- cross join 54 

-- emp2 to emp1
-- inner join 10
-- left join 11
-- right join 13
-- full outer join 14
-- cross join 54


-- for windowing functions

create table emp3
(
    empid1 int,
    emp_sal1 int,
    dept varchar(10)
)

insert into emp3
values
(1,1000,"cs"),
(1,2000,"cs"),
(1,3000,"cs"),
(1,4000,"cs"),
(2,500,"cs"),
(2,1500,"cs"),
(3,5000,"it"),
(4,5000,"it"),
(4,6000,"it"),
(5,8000,"ec"),
(5,9000,"ec"),
(6,10000,"ec")


-- dept wise top salary

/*
select * from (select *, dense_rank() over (partition by dept order by emp_sal1 desc) as r from emp3)
where r = 1
*/

-- cumm sum

/*
select *, sum(emp_sal1) over ( order by emp_sal1) as cumm from Emp3

*/
