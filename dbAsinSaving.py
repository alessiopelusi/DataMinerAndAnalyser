import mysql.connector

def conn():
    mydb = mysql.connector.connect(
        host="<HOST>",
        user="<HOST>",
        password="<PASSWORD>",
        database="<DATABASE_NAME>",
    )
    return mydb

def insert(title, asin, sconto):
    mydb = conn()
    mycursor = mydb.cursor()
    with mycursor:
        if "'" in title: # To fix sintax errors
            title = title.replace("'", " ")
        sql = "INSERT INTO {} (asin, title, discount) VALUES ('{}', '{}', {})".format('<TABLE_NAME>', asin, title, sconto)
        mycursor.execute(sql)
        mydb.commit() # to save changes on the db
        print('Insert Process Ended')