with colony_rank as (
    select id, ntile(4) over (
        order by size_of_colony desc) as rank_group
    from ecoli_data
)
select id,
    case
        when rank_group = 1 then 'CRITICAL'
        when rank_group = 2 then 'HIGH'
        when rank_group = 3 then 'MEDIUM'
        when rank_group = 4 then 'LOW'
    end as colony_name
from colony_rank
order by id