import pyodbc
import logging
import os
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DRIVER")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PWD = os.getenv("PWD")

def create_connection():
    try:
        conn_str = (
            f"DRIVER={DRIVER};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            f"UID={UID};"
            f"PWD={PWD};"
            f"TrustServerCertificate=yes;"
        )
        connection = pyodbc.connect(conn_str)
        logging.info("Successfully connected to the database.")
        return connection
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise
