# Sales_ETL
This project demonstrates a simple ETL pipeline using Python, SQL Server, and CSV files.

**Features:**
* Extract data from CSV files
* Transform data by:
  * Dropping null values.
  * Removing rows with invalid or negative prices
  * Converting date columns
  * Verifying foreign key integrity
  
* Load data into a SQL Server database
* Logs every step of the pipeline

**Requirements:**
* Python 3.8+
* SQL Server (local or cloud)
* ODBC Driver 18 for SQL Server

**Python packages:**

```pip install pandas pyodbc python-dotenv```

**Configuration:**

Create a .env file in the root directory with the following:

```
DRIVER={ODBC Driver 18 for SQL Server}
SERVER=YOUR_SERVER_NAME
DATABASE=SalesDB
UID=YOUR_USER
PWD=YOUR_PASSWORD
```

**How to Run:**

1. Create the database by running schema.sql in SQL SERVER.
2. ```python main.py```
