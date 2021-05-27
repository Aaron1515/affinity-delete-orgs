from api_keys import *

import requests
import csv


count = 0

org_ids = [33107958, 3107957]

for each in org_ids:
  response = requests.delete("https://api.affinity.co/organizations/" + str(each), auth=('', api_key))
  print("Status code: " + str(response.status_code))
  print(response.text.encode('utf8'))

  if response.status_code == 200:
    count = count + 1
    print("Number of notes deleted - " + str(count))
  else:
    print("It failed.")