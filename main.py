import time

# Specify this
powerwallIP = "192.168.2.128"


if __name__ == '__main__':
    print('Trying to connect to the tesla gateway with the IP ' + powerwallIP + '...')
    time.sleep(0.5)
    print('Success!')
