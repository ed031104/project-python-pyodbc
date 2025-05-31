from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT * FROM Orders
                where exists(
                    SELECT c.CustomerID FROM Customers c
                    WHERE c.CustomerID = Orders.CustomerID
                    and Fax IS NOT NULL
                )
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))