 #! /usr/bin/python3.10
 
import psycopg
import example_psql as creds

 sql1 = "select t.table_name, array_agg(c.column_name::text) as columns from information_schema.tables t inner join information_schema.columns c on t.table_name = c.table_name where t.table_schema = 'public' and t.table_type = 'BASE TABLE' and c.table_schema = 'public'  group by t.table_name;"

conn_string = "host=" +  creds.PGHOST + " port=" + "5432" +  " dbname=" + creds.PGDATABASE +  " user=" + creds.PGUSER +  " password=" +  creds.PGPASSWORD

conn = psycopg.connect(conn_string)
cursor = conn.cursor()
cursor.execute(sql1)
tbls = cursor.fetchall()
print("Tables ", tbls)
