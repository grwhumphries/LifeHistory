import webbrowser
import sys
import subprocess
import time

subprocess.Popen(['python', 'C:/LifeHistory/Lifehistory/manage.py', 'runserver'])

time.sleep(4)

url = "http://127.0.0.1:8000"
webbrowser.open(url,new=0)


