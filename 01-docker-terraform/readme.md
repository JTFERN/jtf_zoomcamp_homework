# Question 1
- 25.3

docker run -it \
--rm \
--entrypoint=bash \
python:3.13-slim

pip -V

pip 25.3



# Question 2
- postgres:5433

# Question 3
- 8,007

select count(*) from green
where trip_distance <= 1
and date(lpep_pickup_datetime) between date('2025-11-01') and date('2025-11-30')

# Question 4
- 2025-11-14

select 
lpep_pickup_datetime
, max(trip_distance)
from green
where trip_distance < 100
group by 1
order by max(trip_distance) desc

# Question 5
- East Harlem North

select 
z."Zone"
, count(*)
from green g 
left join zone z on z."LocationID"=g."PULocationID"
group by 1
order by 2 desc

# Question 6
- Yorkville West

select 
z2."Zone"
, max(g.tip_amount)
from green g 
left join zone z on z."LocationID"=g."PULocationID"
left join zone z2 on z2."LocationID"=g."DOLocationID"
where z."Zone"='East Harlem North'
group by 1
order by 2 desc

# Question 7
- terraform init, terraform apply -auto-approve, terraform destroy