with source as (
    select * from {{ ref('raw_campaign_data') }}
)

select
    campaign_id,
    date,
    sum(clicks) as total_clicks,
    sum(impressions) as total_impressions,
    round(sum(cost), 2) as total_cost
from source
group by campaign_id, date
order by date
