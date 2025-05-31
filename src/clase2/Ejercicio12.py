from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT DISTINCT o.ShipName
                FROM Orders o
                WHERE o.Freight = (
                    SELECT MIN(o2.Freight)
                    FROM Orders o2
                    WHERE o2.ShipVia = o.ShipVia
                );
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))