from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                    SELECT * FROM Products
                    WHERE UnitsInStock > (
                        SELECT AVG(UnitsInStock)
                        FROM Products
                    )
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))