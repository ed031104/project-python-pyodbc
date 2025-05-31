from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT * FROM Orders
                WHERE
                    EmployeeID in ( 
                        select 
                            EmployeeID 
                        from 
                            Employees 
                        where 
                            City = 'London'
                    )
                AND
                    CustomerID in (
                        select 
                            Customers.CustomerID 
                        from 
                            Customers 
                        where 
                            Country in ('Spain', 'Mexico', 'Germany') )
                order by Freight desc
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))