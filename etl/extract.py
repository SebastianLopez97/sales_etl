import pandas as pd
import logging

def extract_data():
    try:
        customers = pd.read_csv("assets/customers.csv")
        products = pd.read_csv("assets/products.csv")
        sales = pd.read_csv("assets/sales.csv")

        logging.info("CSV files successfully loaded.")
        return customers, products, sales
    except Exception as e:
        logging.error(f"Failed to load CSV files: {e}")
        raise
