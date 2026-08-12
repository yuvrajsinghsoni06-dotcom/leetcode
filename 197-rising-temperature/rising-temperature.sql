select curr.id
from weather curr
inner join weather nxt
on curr.recordDate = nxt.recordDate + interval '1 day'
and curr.temperature > nxt.temperature;
