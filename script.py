from api_keys import *

import requests
import csv

count = 0

org_ids = [265066382,1515260]

log_file = open("log.csv", "w")
log_file.write("org_id, status code, notes")
log_file.write("\n")

for each in org_ids:
  response = requests.delete("https://api.affinity.co/organizations/" + str(each), auth=('', api_key))

  if response.status_code == 200:
    count = count + 1
    print(str(response.json()))
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + str(response.json()))
    log_file.write("\n")
  else:
  	string_reponse = ''
  	log_file.write(str(each) + ", " + str(response.status_code) + ", " + response.json()[0])
  	log_file.write("\n")

log_file.write("\n")
log_file.write("Number of successful organizations removed: " + str(count))
log_file.close()