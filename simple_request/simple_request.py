import requests
import subprocess
from datetime import datetime

CLOCK_STR = "%H:%M:%S.%f"
now = datetime.now().strftime(CLOCK_STR)

print("Testing semaphore python template")

result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)
if result.stderr:
    print("Errori:", result.stderr)
          
r = requests.get('https://updater.factorio.com/get-available-versions')
with open("/home/luca/factorio-updater/semaphore_python.log", "w") as file:
        file.write(now + " " + str(r))

result = subprocess.run(['cat', '/home/luca/factorio-updater/semaphore_python.log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)
if result.stderr:
    print("Errori:", result.stderr)
