# 單行以逗號分隔元素字串轉為字串陣列
colors_from_user = "#917FB3,#E5BEEC,#FDE2F3"
colors = []
for e in colors_from_user.split(","):
    colors.append(e)
print(colors)

# 多行以逗號分隔元素字串轉為tuple
data_from_user = """201509, 202107, 大學+研究所（文史哲領域）
202107, 202109, 協助學校教授工作"""
data = []
for line in data_from_user.split("\n"):
    data.append(tuple(line.split(",")))
print(data)