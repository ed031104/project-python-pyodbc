from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute(""" 
                SELECT 
                    * 
                FROM 
                    Orders
                WHERE
                    EmployeeID = 3
                AND
                    MONTH(OrderDate) >= 8
                AND
                    MONTH(OrderDate) <= 12
                ORDER BY
                    MONTH(OrderDate) DESC
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))