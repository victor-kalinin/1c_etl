work_bonus = '''
WITH cte AS (
    SELECT period_
    FROM generate_series(:from, :to, '1 month') AS t (period_)
    )
SELECT to_char(period_, 'YYYY-MM-DD"T"HH24:MI:SS') "Period", array_agg(employee) "Employees"
FROM (
    SELECT period_, "Сотрудник" employee, (row_number() over())/50 rn
    FROM rsrc.rs1c_zup_employees
    JOIN cte on cte.period_
    BETWEEN date_trunc('months', "ДатаПриема")
    AND date_trunc('months',
    CASE WHEN "ДатаУвольнения" = '0001-01-01' THEN '3999-12-31' ELSE "ДатаУвольнения" END)
    ) t
GROUP BY period_, rn
'''

reload_queries = ('SELECT nrml.reload_dep_hierarchy();',
                  'SELECT nrml.reload_mstructure_occupation_history();',
                  'SELECT nrml.reload_mstructure_heads_history();')
