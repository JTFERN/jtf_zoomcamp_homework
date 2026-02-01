# Question 1
- 128.3 MiB

# Question 2
- green_tripdata_2020-04.csv

# Question 3
- 24,648,499

SELECT count(*)
FROM `dtc-de-course-484822.zoomcamp.yellow_tripdata` 
WHERE TIMESTAMP_TRUNC(tpep_pickup_datetime, year) = TIMESTAMP("2020-01-01")

# Question 4
- 1,734,051
SELECT count(*)
FROM `dtc-de-course-484822.zoomcamp.green_tripdata` 
WHERE TIMESTAMP_TRUNC(lpep_pickup_datetime, year) = TIMESTAMP("2020-01-01")
# Question 5
- 1,925,152

# Question 6
- Add a timezone property set to America/New_York in the Schedule trigger configuration