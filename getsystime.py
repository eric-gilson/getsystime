import os
import webbrowser

from datetime import date

today = "Today's date : " + str(date.today())
print(today)

strFileNamePath = os.getcwd() + "/python.jpg"
webbrowser.open(strFileNamePath)
