#! /usr/bin/python3.10

import psycopg
import example_psql as creds
import itertools

tbls = []

conn_string = "host=" +  creds.PGHOST + " port=" + "5432" +  " dbname=" + creds.PGDATABASE +  " user=" + creds.PGUSER +  " password=" +  creds.PGPASSWORD
conn = psycopg.connect(conn_string)
cursor = conn.cursor()
cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
tbls = cursor.fetchall()
t1 = list(itertools.chain(*tbls))
print("Tables",t1)
print(t1[0])
# ~ print(cursor.fetchall())

with conn.cursor() as cursor:
	for i in t1:
		cursor.execute("select column_name from information_schema.columns where table_schema = 'public' and table_name='t1[i]'")
		# ~ column_names = cursor.fetchall()
		column_names = [row[0] for row in cursor]
	
print("Cols", column_names)
# ~ print("Column names: {}\n".format(column_names))
