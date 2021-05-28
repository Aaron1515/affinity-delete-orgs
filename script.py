from api_keys import *
from orgs import *

import requests
import csv

count = 0


log_file = open("log.csv", "w")
log_file.write("Organization ID, Status code, Note")
log_file.write("\n")

for each in org_ids:
  response = requests.delete("https://api.affinity.co/organizations/" + str(each), auth=('', api_key))

  if response.status_code == 200:
    count = count + 1
    print("Working on " + str(each) + " - "+ str(response.json()))
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + str(response.json()))
    log_file.write("\n")
  elif response.status_code == 429:
  	print("Working on " + str(each) + " - "+ str(response.json()))
  	break
  elif response.status_code == 500:
  	print("Working on " + str(each) + " - "+ str(response.json()))
  	break
  elif response.status_code == 503:
  	print("Working on " + str(each) + " - "+ str(response.json()))
  	break
  else:
  	print("Working on " + str(each) + " - "+ str(response.json()))
  	log_file.write(str(each) + ", " + str(response.status_code) + ", " + response.json()[0])
  	log_file.write("\n")

log_file.write("\n")
log_file.write("Number of successful organizations removed: " + str(count))
log_file.close()