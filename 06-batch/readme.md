# Question 1
- '4.1.1'


# Question 2
- 25MB

# Question 3
-  162604

df_result = spark.sql("""
SELECT 
    count(*)
FROM
    yellow
WHERE
    date_trunc('day',tpep_pickup_datetime)= date '2025-11-15'
""")

# Question 4
- 90.6

SELECT 
    trip_distance,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    (unix_timestamp( tpep_dropoff_datetime)-unix_timestamp( tpep_pickup_datetime))/3600 as hours
FROM
    yellow
order by 4 desc

# Question 5
- 4040

# Question 6
- Governor's Island/Ellis Island/Liberty Island

SELECT 
    Zone,
    count(PULocationID)
FROM
    yellow
left join zone on yellow.PULocationID= zone.LocationID
group by 1
order by 2 asc
