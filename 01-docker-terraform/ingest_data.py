#import os
import pandas as pd
from sqlalchemy import create_engine
#import time

# Wait for PostgreSQL to be ready
#time.sleep(10)  # optional; simple approach

# Connection info from env
POSTGRES_USER ='root'
POSTGRES_PASSWORD ='root'
POSTGRES_DB ='ny_taxi'
POSTGRES_HOST ='pgdatabase'

# Connect to PostgreSQL
engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}")
csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
parquet_url='https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
# Load CSV
df_csv = pd.read_csv(csv_url)
df_csv.to_sql(name="zone", con=engine, if_exists="replace", index=False)
print("CSV file loaded into table 'zone'.")

# Load Parquet
df_parquet = pd.read_parquet(parquet_url)
df_parquet.to_sql(name="green", con=engine, if_exists="replace", index=False)
print("Parquet file loaded into table 'green'.")