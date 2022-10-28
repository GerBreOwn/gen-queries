#! /usr/bin/python3.10

import psycopg
import example_psql as creds
import itertools
import get_names

dt = ["hour", "date", "month", "year"]

def build_queries(names):
	
	sql1a = f"select "
	sql1b = f" list columns"
	sql1c = f" from {names[0]} where  created >= {dt[0]}"
	sql1 = sql1a + sql1b + sql1c
	print(sql1)
	
	sql2a = f"select extract {dt[0]} from created as {dt[0]}, "
	sql2b = f"list columns"
	sql2c = f"from etc, group by {dt[0]} order by {dt[0]} where created >= {dt[0]}"

def main():
	global names
	tnames = get_names.sql_names()
	print("TNAMES",tnames)
	# ~ c_names = get_names(k)
	build_queries(tnames)
	
if __name__ == "__main__":
	main()


