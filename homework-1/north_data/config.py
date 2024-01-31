from pathlib import Path
import os

CUSTOMER = Path(__file__).parent.joinpath('customers_data.csv')
EMPLOYEES = Path(__file__).parent.joinpath('employees_data.csv')
ORDERS = Path(__file__).parent.joinpath('orders_data.csv')

DATA = (CUSTOMER, EMPLOYEES, ORDERS)
NAME_BD = ('customers_data', 'employees_data', 'orders_data')