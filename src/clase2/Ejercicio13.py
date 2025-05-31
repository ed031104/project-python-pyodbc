from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT DISTINCT 
                    Orders.OrderID,
                    [Order Details].ProductID,
                    [Order Details].[Quantity],
                    [Products].ProductName
                FROM [Orders]
                Inner JOIN [Order Details] ON [Orders].OrderID = [Order Details].OrderID
                INNER JOIN Products ON [Order Details].ProductID = Products.ProductID
                WHERE
                    [Products].[ProductName] like '%o%'
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))