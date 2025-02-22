select fi.id, fni.fish_name, fi.length
from fish_info fi
join fish_name_info fni on fi.fish_type = fni.fish_type
where fi.fish_type in (
    select fish_type
    from fish_info
    group by fish_type
    having length = max(length)
)
order by fi.id