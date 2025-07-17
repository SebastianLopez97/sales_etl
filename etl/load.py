import logging

def load_data(customers, products, sales, connection):
    cursor = connection.cursor()

    try:
        for _, row in customers.iterrows():
            cursor.execute("""
                INSERT INTO Customers (CustomerID, Name, Email, City)
                VALUES (?, ?, ?, ?)
            """, row["CustomerID"], row["Name"], row["Email"], row["City"])

        for _, row in products.iterrows():
            cursor.execute("""
                INSERT INTO Products (ProductID, ProductName, Category, Price)
                VALUES (?, ?, ?, ?)
            """, row["ProductID"], row["ProductName"], row["Category"], row["Price"])

        for _, row in sales.iterrows():
            cursor.execute("""
                INSERT INTO Sales (SaleID, CustomerID, ProductID, SaleDate, Quantity)
                VALUES (?, ?, ?, ?, ?)
            """, row["SaleID"], row["CustomerID"], row["ProductID"], row["SaleDate"], row["Quantity"])

        connection.commit()
        logging.info("Data successfully loaded into the database.")
    except Exception as e:
        logging.error(f"Error loading data into the database: {e}")
        connection.rollback()
        raise
    finally:
        cursor.close()
