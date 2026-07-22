select
    a.client_id
from account a
left join "transaction" t
    on t.account_id = a.id
    and t.type = 'BUY'
    and t.transaction_date >= current_date - interval '1 month'
    and t.transaction_date < current_date
group by a.client_id
having coalesce(sum(t.amount), 0) < 5000
order by a.client_id;
