import requests
from datetime import datetime
CLOCK_STR = "%H:%M:%S.%f"
now = datetime.now().strftime(CLOCK_STR)
print("Testing semaphore python template")
r = requests.get('https://updater.factorio.com/get-available-versions')
print(now + " " + str(r))
with open("semaphore_python.log", "w") as file:
        file.write(now + " " + str(r))
