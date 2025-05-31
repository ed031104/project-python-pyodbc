from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT * FROM Orders
                WHERE
                    orders.EmployeeID in (
                        select EmployeeID from Employees where City = 'Seattle'
                    )
                and
                Freight > (
                    select max(Freight) from Orders
                    WHERE ShipCountry = 'Spain'
                )
                and
                    year(orders.OrderDate) = 1994
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))