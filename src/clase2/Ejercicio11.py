from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT DISTINCT ShipName
                FROM Orders
                JOIN Shippers ON Orders.ShipVia = Shippers.ShipperID
                WHERE Shippers.CompanyName = 'Speedy Express';
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))