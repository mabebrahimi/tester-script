import os
import sys
from urllib.parse import urlparse
import mysql.connector

# read DWS_MYSQL_DATABASE_URI env from os
DWS_MYSQL_DATABASE_URI = os.getenv('DWS_MYSQL_DATABASE_URI')

# check DWS_MYSQL_DATABASE_URI env exist
if DWS_MYSQL_DATABASE_URI is None:
    print("please insert 'DWS_MYSQL_DATABASE_URI' env")
    quit()

# try to connect
try:
    dbc = urlparse(DWS_MYSQL_DATABASE_URI)
    
    cnx = mysql.connector.connect(user=dbc.username, password=dbc.password,
                                  host=dbc.hostname, port=dbc.port,
                                  database=dbc.path.lstrip('/'))
    
except Exception as e:
    print(f"Error msg: {e}")
    print(1, file=sys.stderr)
else:
    print(0)

