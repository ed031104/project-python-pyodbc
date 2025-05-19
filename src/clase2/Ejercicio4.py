from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT 
                    CategoryID [ID de la categoria],
                    SupplierID [ID del proveedor],
                    max(UnitPrice) [Precio mas caro],
                    AVG(UnitPrice) [Precio promedio],
                    count(UnitPrice) [cantidad de precios de productos],
                    sum(UnitPrice) [suma de precios de productos]
                FROM 
                    Products
                GROUP BY
                    CategoryID, SupplierID
                ORDER BY
                    CategoryID, SupplierID asc
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))