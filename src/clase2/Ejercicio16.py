from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT * FROM Orders
                where exists(
                    SELECT e.EmployeeID FROM Employees e
                    WHERE e.EmployeeID = Orders.EmployeeID
                    and e.Country <> 'UK'
                )
                """)

columns = [column[0] for column in cursor.description]

print(tabulate(cursor.fetchall(), headers=columns, tablefmt="psql"))