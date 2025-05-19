from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                select
                    Country,
                    City,
                    COUNT(CustomerID) as [CantidadClientes]
                from 
                    Customers
                WHERE
                    City LIKE 'm%'
                    OR
                    City LIKE 'l%'
                    OR
                    City LIKE '%e'
                GROUP by Country, City
                HAVING
                    COUNT(CustomerID) > 3;
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))