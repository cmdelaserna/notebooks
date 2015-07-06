#import  csv file

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import sys
import pprint

url = '../data/first-look-vc/test-matter.csv'

try:
	data = pd.read_csv(url)
	print data.info()
	print "======="
	print data[:1]
	print "======="
except:
	print "error reading csv file"

#cities
cities_count = data['City'].value_counts()
print cities_count
cities_count.plot[:10](kind='barh', rot=0)



# try:
# 	with open(filename, 'rU') as f:
# 		reader = csv.reader(f)
# 		header = reader.next()
# 		data = [row for row in reader]
# except csv.Error as e:
# 	print "Error reading csv file in line %s: %s" % (reader.line_num, e)
# 	sys.exit(-1)
# if header: 
# 	print header
# 	print '==============='

# print [i for i in data]