from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT 
                    CategoryID,
                    min(UnitPrice) [Precio Mínimo]
                FROM 
                    Products
                GROUP BY
                    CategoryID
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))