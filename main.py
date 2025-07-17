import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.db import create_connection


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("ETL process started")

    try:
        customers, products, sales = extract_data()
        logging.info("Data extracted")

        customers, products, sales = transform_data(customers, products, sales)
        logging.info("Data transformed")

        connection = create_connection()
        load_data(customers, products, sales, connection)
        connection.close()
        logging.info("Data loaded into the database")

    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()
