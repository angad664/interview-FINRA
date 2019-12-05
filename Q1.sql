select
a.conv_date as ORIGINAL_DATE,
case when date_format(a.conv_date,'u')=7 then a.conv_date
     else date_format(a.conv_date,'u') <> 7 then a.conv_date+(7-date_format(a.conv_date,'u')) end as END_OF_WEEK,
from_unixtime(unix_timestamp( last_day(a.conv_date),'yyyy-MM-dd'), 'yyyyMMdd') as END_OF_MONTH

(select
from_unixtime(unix_timestamp( orig_date,'yyyyMMdd'), 'yyyy-MM-dd') as conv_date
from original_date) a
