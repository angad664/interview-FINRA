select
id,
start_time,
end_time,
select group_id from table_1 tb1 inner join table_1 tb2 on

case when  tb2.start_time>tb1.start_time  or tb2.end_time<tb2.start_time then rank over(order by id) group_id
     else FLOOR(RAND()*(1000000-5+1)+5) as group_id

Note - here table_1 is the source table
