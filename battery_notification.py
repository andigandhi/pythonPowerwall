import time
import requests
import urllib3
from notify_run import Notify

# Time between the requests
powerwallIP = "192.168.2.127"
notifyID = "XXXXXXXX"
timeInterval = 60

fullyCharged = False


def getFromPowerwall():
    response = requests.get("https://" + powerwallIP, verify=False)
    text = response.json()
    return text["percentage"]


def sendNotification():
    print("Your powerwall is now fully charged!")
    notify = Notify(endpoint="https://notify.run/"+notifyID)
    notify.send("Your powerwall is now fully charged!")


if __name__ == '__main__':
    print('Trying to connect to the powerwall ' + powerwallIP + '...')
    urllib3.disable_warnings()
    powerwallIP += "/api/system_status/soe"

    while 1:
        charge = getFromPowerwall()
        if charge > 99 and not fullyCharged:
            sendNotification()
            fullyCharged = True
        elif charge < 95:
            fullyCharged = False

        time.sleep(timeInterval)
