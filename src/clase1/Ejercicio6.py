from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("select * from dbo.[Orders] where EmployeeID in (2,5,7) and Orders.OrderDate like '%1996%' order by EmployeeID desc")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))