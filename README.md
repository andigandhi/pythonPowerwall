<p align="center">
  <img src="https://raw.githubusercontent.com/andigandhi/pythonPowerwallTools/master/.github/banner.png">
</p>
Different tools for the Tesla Powerwall written in Python.

## sql_log.py
Logs the power production and consumption into a SQL database
The SQL login data and the IP of the powerwall has to be adjusted in the first lines of the script.

## battery_notification.py
This script sends a push notification to your smartphone whenever the battery is fully charged.
This is useful as often it is financially more interesting to use the power by oneself than to deliver it to the power grid.
The notification is done with the notify.run service which can be installed via `pip install notify-run`.
