import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] == "temp":
            pass
        else:
            temperatures.append( int(row[1]))

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
res = data["Primary Fur Color"].value_counts()
print(res)
res.to_csv("new_data.csv")
# res1 = data[data["Primary Fur Color"] == "Gray"]
# print(len(res1))
# with open("new_data.csv")as first:
#     dod = first.readlines()
#     print(dod)
