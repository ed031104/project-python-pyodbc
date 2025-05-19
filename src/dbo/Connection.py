import pyodbc
from dotenv import  load_dotenv
import os

class Connection:

    def connection(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
        load_dotenv(dotenv_path=dotenv_path)

        server_name = os.getenv('NAME_SERVER')
        database = os.getenv('DATABASE')
        name = os.getenv('NAME_SERVER')
        print(server_name, database)

        if not server_name or not database:
            raise ValueError("Las variables de entorno NAME_SERVER y/o DATABASE no están definidas.")

        connect = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server_name};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
        )
        return connect