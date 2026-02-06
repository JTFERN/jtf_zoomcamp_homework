CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-484822.zoomcampdwhw3.external_yellow_tripdata`
  OPTIONS (
    format ="PARQUET",
    uris = ['_____*.parquet']
    );

CREATE TABLE `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata` AS (
  SELECT
   *
  FROM
    `dtc-de-course-484822.zoomcampdwhw3.external_yellow_tripdata`
);

# Question 1
- 20,332,093

select count (*)
from `dtc-de-course-484822.zoomcampdwhw3.external_yellow_tripdata`

# Question 2
- 0 MB for the External Table and 155.12 MB for the Materialized Table

select count (distinct PULocationID)
from `dtc-de-course-484822.zoomcampdwhw3.external_yellow_tripdata`;


select count (distinct PULocationID)
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`;

# Question 3
- BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

select PULocationID
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`;

select PULocationID, DOLocationID
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`;

# Question 4
- 8,333

select count(*)
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`
where fare_amount=0;

# Question 5
- Partition by tpep_dropoff_datetime and Cluster on VendorID

CREATE OR REPLACE TABLE `dtc-de-course-484822.zoomcampdwhw3.five_external_yellow_tripdata`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `dtc-de-course-484822.zoomcampdwhw3.external_yellow_tripdata`;

# Question 6
- 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

select distinct VendorID
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`
where TIMESTAMP_TRUNC(tpep_dropoff_datetime,day)> TIMESTAMP("2024-03-01") and TIMESTAMP_TRUNC(tpep_dropoff_datetime,day)<=TIMESTAMP("2024-03-15");

select distinct VendorID
from `dtc-de-course-484822.zoomcampdwhw3.five_external_yellow_tripdata`
where TIMESTAMP_TRUNC(tpep_dropoff_datetime,day)> TIMESTAMP("2024-03-01") and TIMESTAMP_TRUNC(tpep_dropoff_datetime,day)<=TIMESTAMP("2024-03-15");

# Question 7
- GCP Bucket


# Question 8
- False

# Question 9
- 0


select count(*)
from `dtc-de-course-484822.zoomcampdwhw3.yellow_tripdata`;