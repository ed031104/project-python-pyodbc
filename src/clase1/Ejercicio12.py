from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("select * from dbo.[Products] where Discontinued = 0 and UnitPrice > 35 and UnitPrice <= 190 and CategoryID in (1,3,4,7,8) and SupplierID in (2,4,6,7,9)")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))