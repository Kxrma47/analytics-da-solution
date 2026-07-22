select
    id,
    scores,
    rank() over (order by scores desc) as rating_position
from examination
order by rating_position, id;
