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

column_names = []
x = len(t1)
with conn.cursor() as cursor:
	for i in range (x):
		# ~ print("T1", t1[i])
		y = t1[i]
		print("Y", y)
		ce = f"select column_name from information_schema.columns where table_schema = 'public' and table_name= '{y}'"
		print("CE",ce)
		cursor.execute("select column_name from information_schema.columns where table_schema = 'public' and table_name='y'")
		# ~ column_names = cursor.fetchall()
		column_names.append([row[0] for row in cursor])
	
print("Cols", column_names)
# ~ print("Column names: {}\n".format(column_names))
