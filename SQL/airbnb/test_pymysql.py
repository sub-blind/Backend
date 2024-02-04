import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="rla456852",
    db="classicmodels",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


# . SELECT * FROM
def get_customers():
    cur = connection.cursor()
    sql = "SELECT * FROM customers"
    cur.execute(sql)
    customers = cur.fetchone()
    print("customer : ", customers)
    print("customer : ", customers["customerNumber"])
    print("customer : ", customers["customerName"])
    print("customer : ", customers["country"])
    cur.close()


# INSERT INTO customers
def add_customer():
    cur = connection.cursor()
    name = "JaeSeop"
    family_name = "Kim"
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({10001}, '{name}', '{family_name}')"
    cur.execute(sql)
    connection.commit()
    cur.close()


# add_customer()


# 3. UPDATE INTO
def upadate_customer():
    cur = connection.cursor()
    update_name = "update_kim"
    contactLastName = "update_seop"
    sql = f"UPDATE customers SET customerName = '{update_name}', contactLastName = '{contactLastName}' WHERE customerNumber = 10000"
    cur.execute(sql)
    connection.commit()
    cur.close()


# upadate_customer()


# 4. DELETE FROM
def delete_customer():
    cur = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 10000"
    cur.execute(sql)
    connection.commit()
    cur.close()


delete_customer()
