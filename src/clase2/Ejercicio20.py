from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT * FROM Orders
                WHERE
                Freight < (
                    select avg(Freight) from Orders
                    WHERE ShipCountry = 'Spain'
                )
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))