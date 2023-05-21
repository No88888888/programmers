SELECT
PT_NAME,
GEND_CD,
AGE,
case when TLNO = 'null' then "NONE" END AS TLNO
FROM PATIENT
where GEND_CD = 'W' and age <= 12
order by AGE desc, PT_NAME asc;