from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                select 
                    o.OrderID as [ID Orden],
                    COUNT(od.ProductID) as [Numero de pedido]
                from 
                    [Orders] o
                JOIN 
                    [Order Details] od
                ON
                    o.OrderID = od.OrderID
                GROUP BY
                    o.OrderID
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))