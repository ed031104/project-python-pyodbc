from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""SELECT
                    *
                FROM
                    Products
                where
                    Discontinued = 1
                    and
                        SupplierID in (1,3,7,8,9)
                    and
                        UnitsInStock > 0
                    and
                        UnitPrice >= 39
                    and
                        UnitPrice <= 190
                order by
                    SupplierID, UnitPrice asc
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="rst"))