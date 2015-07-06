#import json file using requests

import requests
import json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from pprint import pprint

url = 'https://api.github.com/events'

r = requests.get(url)
data = json.loads(r.text)

#all data
pprint(data[0])

print ("==========")

# get a nested record
pprint(data[0]['actor']['login'])

print ("==========")

#get all user logins
logins = [log['actor']['login'] for log in data]
print logins

print ("==========")

frame = DataFrame(logins)
print frame