﻿from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("select * from dbo.Customers order by ContactName asc")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))