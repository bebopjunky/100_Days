# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             tmp = row[1]
#             temperatures.append(int(tmp))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# # avg = 0
# # for temp in temp_list:
# #     avg += temp
# #
# # avg = avg / len(temp_list)
# avg = data["temp"].mean()
# print(avg)

#print(data["temp"].max())

#print(data[data.temp == data.temp.max()])

sunday = data[data.day == "Sunday"]

print(sunday.temp * (9/5) + 32)