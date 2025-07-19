

import pymysql
pymysql.install_as_MySQLdb()
from agno.storage.mysql import MySQLStorage
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DB_URL")

storage = MySQLStorage(
    table_name="agent_sessions",
    db_url=db_url,
    auto_upgrade_schema=True,
)