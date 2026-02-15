# Question 1
- int_trips_unioned only


# Question 2
- dbt will fail the test, returning a non-zero exit code

# Question 3
- 12,184
select count(*)
from taxi_rides_ny.prod.fct_monthly_zone_revenue

# Question 4
- East Harlem North

select pickup_zone
, sum(revenue_monthly_fare)
from taxi_rides_ny.prod.fct_monthly_zone_revenue
where 1=1
and service_type like 'Green'
and date_trunc('year',revenue_month)= date '2020-01-01'
group by 1
order by 2 desc

# Question 5
- 384,624

select sum(total_monthly_trips)
from taxi_rides_ny.prod.fct_monthly_zone_revenue
where 1=1
and service_type like 'Green'
and revenue_month= date '2019-10-01'

# Question 6
- 43,244,693

Ingest data using ingest_hw.py
Create a stg model like stg_fhv

Select count(*) from model