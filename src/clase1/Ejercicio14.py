from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""  SELECT top 7
                        * 
                    FROM 
                        Products 
                    where
                        UnitsInStock > 0
                    order by UnitPrice desc""")

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))