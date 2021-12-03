3/a)
select s.city, sum(s.commission) sum_of_commission
from salesman s
group by s.city

3/b)
select * from customer c
join salesman s on c.salesman_id = s.salesman_id
where s.commission > 0.12
order by s.commission


