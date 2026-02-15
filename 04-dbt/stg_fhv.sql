with source as (
    select * from {{ source('raw', 'fhv_tripdata') }}
)

select *
from source
where dispatching_base_num IS not NULL