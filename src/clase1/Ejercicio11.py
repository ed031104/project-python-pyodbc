from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("select * from dbo.[Suppliers] where CompanyName not in(select CompanyName from Suppliers SList where SList.CompanyName  >= 'B' and SList.CompanyName <= 'h') and Country like '%UK%' order by CompanyName asc")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))