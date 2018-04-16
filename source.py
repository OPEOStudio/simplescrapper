import csv

# Base population in the world

# Base population in the world has been generated thanks to various sources
# For more accuracy go directly to the XLS file

with open('180412 - baseinfo CSV - Population.csv', 'rb') as csvfile:
    database = csv.reader(csvfile, delimiter=' ', quotechar='|')

print(database)
