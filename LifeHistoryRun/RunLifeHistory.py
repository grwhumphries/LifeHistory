import webbrowser
import sys
import subprocess

subprocess.Popen(['python', 'C:/LifeHistory/Lifehistory/manage.py', 'runserver'])

url = "http://127.0.0.1:8000"
webbrowser.open(url,new=0)


