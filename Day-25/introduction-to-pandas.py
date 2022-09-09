# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# # To get hold of each column
# print(data["temp"]) 
# print(data)

# # Finding average
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].mean())
# # Finding maximum
# print(data["temp"].max())
# # ALternative way of getting hold of columns (automatic conversion of first row values into attributes [Case sensitive] by Pandas)
# print(data.temp)

# Get data from each row
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data[data.day == "Monday"])
# # Printing day wherein temp is max
# print(data[data.temp == data.temp.max()])

# Convert temp from celsius to farenheit 
import pandas
data = pandas.read_csv("weather_data.csv")
print(int(data.temp[data.day == "Monday"]) * 9 / 5 + 32)

# Creating dataframe from scratch
data_dict = {
    "students" : ["Amy", "James"],
    "scores" : [75, 98]
}

data = pandas.DataFrame(data_dict)
print(data)
# Creating a csv file
data.to_csv("new_data.csv")