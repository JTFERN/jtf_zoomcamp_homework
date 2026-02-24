# Question 1
- 2009-06-01 to 2009-07-01

SELECT
  min(trip_dropoff_date_time)
  , max(trip_dropoff_date_time)
FROM "nyc_taxi_trips"


# Question 2
- 26.66%

select count(*) as total, sum(case when payment_type = \'Credit\' then 1 else 0 end) as credit from nyc_taxi_trips

# Question 3
- $6,063.41

select sum(tip_amt) from nyc_taxi_trips


