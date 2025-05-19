from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT 
                    Country [pais],
                    CustomerID [codigo cliente]
                FROM 
                    [Orders Qry]
                GROUP BY 
                    Country,
                    CustomerID
                HAVING
                    Country in ('Venezuela', 'Brazil')
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))