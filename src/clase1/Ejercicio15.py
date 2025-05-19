from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute(""" 
                SELECT top 9
                    * 
                FROM 
                    Products 
                where
                    CategoryID in (3,5,8)
                order by UnitsInStock asc
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))