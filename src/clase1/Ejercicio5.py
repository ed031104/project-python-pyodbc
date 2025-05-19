from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("select * from dbo.[Products] where Discontinued = 1 and UnitsInStock = 0 and CategoryID not in (1,3,4,7)")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))