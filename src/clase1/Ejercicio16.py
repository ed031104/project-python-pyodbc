from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute(""" 
                SELECT 
                    * 
                FROM 
                    Orders
                where
                    EmployeeID >= 2
                AND 
                    EmployeeID <= 5
                AND
                    CustomerID >= 'A'
                AND
                    CustomerID < 'H'
                AND
                    MONTH(OrderDate) = 7
                AND
                    DAY(OrderDate) = 31
                order by CustomerID asc
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))