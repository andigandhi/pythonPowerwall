import time
import requests
import urllib3
import mysql.connector

# Specify this

# IP Address of the tesla powerwall
powerwallIP = "https://192.168.2.127"
# Time between the requests
timeInterval = 30
# connection data of the database
mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    password="PASSWORD",
)

# Start of the actual code

mycursor = mydb.cursor()


def commitToDb(data):
    sql = "INSERT INTO powerData (solar, house, battery, grid) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()


def getFromPowerwall():
    response = requests.get(powerwallIP, verify=False)
    text = response.json()
    return (text["solar"]["instant_power"], text["load"]["instant_power"], text["battery"]["instant_power"], text["site"]["instant_power"])


if __name__ == '__main__':
    print('Trying to connect to the database at ' + mydb.server_host + '...')
    mycursor.execute("USE tesla_powerwall;")

    mycursor.execute("DROP TABLE powerData")
    mycursor.execute("CREATE TABLE powerData (time TIMESTAMP, solar SMALLINT(255), house SMALLINT(255), battery SMALLINT(255), grid SMALLINT(255))")

    print('Trying to connect to the powerwall ' + powerwallIP + '...')
    urllib3.disable_warnings()
    powerwallIP += "/api/meters/aggregates"

    while 1:
        commitToDb(getFromPowerwall())
        time.sleep(timeInterval)

