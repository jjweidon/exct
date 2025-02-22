with recursive rec as (
    select id, parent_id, 1 as generation
    from ecoli_data
    where parent_id is null
    union
    select ed.id, ed.parent_id, rec.generation+1
    from ecoli_data ed
    join rec on rec.id = ed.parent_id
)
select count(*) count, generation
from rec
where id not in (
    select distinct parent_id
    from rec
    where parent_id is not null
)
group by generation
order by generation