-- SQL-команды для создания таблиц
CREATE TABLE customers_data (customer_id text, company_name text, contact_name text);
CREATE TABLE employees_data (employee_id int, first_name text, last_name text, title text, birth_date date, notes text);
CREATE TABLE orders_data (order_id int, customer_id text,employee_id int, order_date date, ship_city text);

