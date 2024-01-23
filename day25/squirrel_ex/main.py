import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240123.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrels = {"Fur Color": ["gray", "red", "black"],
             "Count": [gray_squirrels, red_squirrels, black_squirrels]}

pandas.DataFrame(squirrels).to_csv("squirrel_count")
