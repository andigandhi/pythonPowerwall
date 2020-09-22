import mysql.connector

# Specify this
powerwallIP = "192.168.2.128"

mydb = mysql.connector.connect(
    host="192.168.2.199",
    user="pi",
    password="munichopen",
)
mycursor = mydb.cursor()


def commitToDb(data):
    sql = "INSERT INTO powerData (solar, house, battery, grid) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()


if __name__ == '__main__':
    # mycursor.execute("CREATE TABLE powerData (time TIMESTAMP, solar TINYINT(255), house TINYINT(255), battery TINYINT(255), grid TINYINT(255))")

    mycursor.execute("USE tesla_powerwall;")
    mycursor.execute("SELECT * FROM powerData;")
    myresult = mycursor.fetchall()
    print(myresult)
    #commitToDb([1, 2, 3, 4])

    exit()
    print('Trying to connect to the database at ' + mydb.server_host + '...')
    print('Success!')
    print('Trying to connect to the powerwall ' + powerwallIP + '...')
    print('Success!')

