import mysql.connector

def ConnectorMysql():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db",
        # auth_plugin='mysql_native_password'
    )
    return mydb

# All DATA
def get_data(nogun):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT * FROM gun WHERE nogun='{}';".format(nogun))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        arr = {
            "nogun": x[0],
            "uname": x[1],
            "pickup": int(x[2]),
            "broken": x[3],
            "lost": x[3],
            "remaining": x[3]
        }
    return arr

def get_alldata():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT * FROM gun")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    print(myresult)
    return myresult


# SUM PICKUP
def get_pickup():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT SUM(pickup)FROM gun;")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:

        print(x)
    return x

# SUM LOST
def get_lost():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT SUM(lost)FROM gun;")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    return x

# SUM BROKEN
def get_broken():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT SUM(broken)FROM gun;")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    return x

# SUM REMAINING
def get_remaining():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT SUM(remaining)FROM gun;")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    return x

# input
# localhost:5000/insert?uname=C&pickup=0&broken=1&lost=0&remaining=0&nogun=3
def insert_data(uname, pickup, broken, lost, remaining, nogun):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO gun (uname, pickup, broken, lost, remaining, nogun) VALUES (%s ,%s, %s,%s, %s, %s)"
    val = (uname, pickup, broken, lost, remaining, nogun)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()


# localhost:5000/update?pickup=0&broken=1&lost=0&remaining=0&nogun=1
def update_data( pickup, broken, lost, remaining, nogun):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE gun SET pickup=%s , broken=%s , lost=%s , remaining=%s  WHERE nogun=%s"
    val = (pickup, broken, lost, remaining, nogun)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()

# localhost:5000/delete?nogun=3
def delete_data(nogun):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE  FROM gun WHERE nogun={}".format(nogun)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
