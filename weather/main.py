# from time import process_time_ns
#
import pandas
#
# data = pandas.read_csv('weather_data.csv')
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# #
# # # aver_temp = sum(temp_list) / len(temp_list)
# # # print(aver_temp)
# #
# # print(data["temp"].mean())
# #
# # # max_value = max(data["temp"].to_list())
# # # print(max_value)
# # print(data["temp"].max())
# #
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
#
#

data = pandas.read_csv("4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")