from src.dbo.Connection import Connection
from tabulate import tabulate

cursor = Connection().connection().cursor()
cursor.execute("""
                SELECT
                    c.CategoryID,
                    c.CategoryName,
                    s.SupplierID,
                    s.CompanyName,
                    AVG(p.UnitPrice) AS AvgPrice,
                    MAX(p.UnitPrice) AS MaxPrice
                FROM 
                    Products p
                JOIN Categories c ON p.CategoryID = c.CategoryID
                JOIN Suppliers s ON p.SupplierID = s.SupplierID
                GROUP BY
                    c.CategoryID,
                    c.CategoryName,
                    s.SupplierID,
                    s.CompanyName
                HAVING
                    AVG(p.UnitPrice) BETWEEN 10 AND 20
                    OR MAX(p.UnitPrice) >= 80;
                """)

columns = [column[0] for column in cursor.description]

print (tabulate(cursor.fetchall(), headers=columns ,tablefmt="psql"))