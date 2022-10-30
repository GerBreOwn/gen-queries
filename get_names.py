#! /usr/bin/python3.10
 
import psycopg
import example_psql as creds

names = []
c = []
t = []

def sql_names():
	sql1_get_names = "select t.table_name, array_agg(c.column_name::text) as columns from information_schema.tables t inner join information_schema.columns c on t.table_name = c.table_name where t.table_schema = 'public' and t.table_type = 'BASE TABLE' and c.table_schema = 'public'  group by t.table_name;"
	conn_string = "host=" +  creds.PGHOST + " port=" + "5432" +  " dbname=" + creds.PGDATABASE +  " user=" + creds.PGUSER +  " password=" +  creds.PGPASSWORD
	conn = psycopg.connect(conn_string)
	cursor = conn.cursor()
	cursor.execute(sql1_get_names)
	tbls = cursor.fetchall()
	names = [list(ele) for ele in tbls]
	for table in names:
		for col in table:
			print(col,)
			for itm in col:
				if itm == "id" or itm == "created":
					continue
				# ~ c.append(itm)
				# ~ print(c)
		# ~ print
		
	
def main():
	sql_names()
	

if __name__ == "__main__":
	main()
