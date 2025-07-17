import pandas as pd
import logging

def transform_data(customers, products, sales):
    null_customers = customers.isnull().sum().sum()
    if null_customers > 0:
        logging.info(f"{null_customers} null values found in customers — rows dropped.")
        customers = customers.dropna()

    null_products = products.isnull().sum().sum()
    if null_products > 0:
        logging.info(f"{null_products} null values found in products — rows dropped.")
        products = products.dropna()

    null_sales = sales.isnull().sum().sum()
    if null_sales > 0:
        logging.info(f"{null_sales} null values found in sales — rows dropped.")
        sales = sales.dropna()

    negative_prices = len(products[products["Price"] < 0])
    if negative_prices > 0:
        logging.info(f"{negative_prices} negative prices found — rows dropped.")
        products = products[products["Price"] >= 0]

    sales["SaleDate"] = pd.to_datetime(sales["SaleDate"], errors="coerce")
    sales = sales.dropna(subset=["SaleDate"])

    missing_customers = ~sales["CustomerID"].isin(customers["CustomerID"])
    missing_products = ~sales["ProductID"].isin(products["ProductID"])

    if missing_customers.any():
        count = missing_customers.sum()
        logging.info(f"{count} sales with invalid CustomerID — rows dropped.")
        sales = sales[~missing_customers]

    if missing_products.any():
        count = missing_products.sum()
        logging.info(f"{count} sales with invalid ProductID — rows dropped.")
        sales = sales[~missing_products]

    return customers, products, sales
