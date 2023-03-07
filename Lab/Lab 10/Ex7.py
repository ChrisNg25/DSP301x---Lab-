import re

str="""Some of the prices were as following TSLA:749.50, ORCL: 50.50, GE: 10.90, MSFT: 170.50, BIDU: 121.40. As the macroeconomic developments continue we will update the prices. """

#Type your answer here.

regex = '([A-Z]+):'  # lọc các chuỗi chữ cái viết hoa, kết thúc bằng dấu hai chấm, phần trong ngoặc tròn được findall
data = re.findall(regex, str)
for i in range(len(data)):
	data[i] = data[i].replace(':','')
print(data)
