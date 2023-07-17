import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "fur": ["Cinnamon","Gray","Black"],
    "count": [cinnamon,gray,black]
}

data_csv = pandas.DataFrame(data_dic)
data_csv.to_csv("squirrel_data.csv")