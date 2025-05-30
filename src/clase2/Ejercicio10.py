﻿from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                select 
                CONCAT(Discount * 100, '%') [Decuento de detalles de pedidos] 
                FROM    
                    [Order Details]
                GROUP BY
                    Discount
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))