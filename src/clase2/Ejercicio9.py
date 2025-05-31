from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                select *
                FROM    
                    Orders
                WHERE   
                    Freight < 1
                AND
                    year(OrderDate) = 1994
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))