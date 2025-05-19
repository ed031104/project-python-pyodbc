from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute(""" 
                SELECT 
                    * 
                FROM 
                    [Order Details]
                WHERE
                    Quantity BETWEEN 10 AND 250
                ORDER by 
                    Quantity DESC
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))