# Dependency needed to install file 

# !pip install xlrd
# Import required library

import pandas as pd

csv_path = 'TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
'''Chúng ta có thể sử dụng phương thức head() để kiểm tra 5 hàng đầu của khung dữ liệu:'''
# Print first five rows of the dataframe

print(df.head())

'''Chúng ta sử dụng đường dẫn của tệp excel và hàm read_excel. Kết quả được một khung dữ liệu như trước:'''
# Read data from Excel File and print the first five rows

xlsx_path = 'TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
print(df.head())
'''Chúng ta có thể truy cập cột Length và gán cho nó một khung dữ liệu mới x:'''
# Access to the column Length

x = df[['Length']]
print(x)
'''Xem và truy cập dữ liệu
Bạn cũng có thể lấy một cột dưới dạng một chuỗi. Bạn có thể coi chuỗi Pandas là khung dữ liệu 1-D. 
Chỉ cần sử dụng một dấu ngoặc:

'''
# Get the column as a dataframe

x = type(df[['Artist']])
print(x)
'''Bạn có thể làm điều tương tự cho nhiều cột; chúng ta chỉ đặt tên khung dữ liệu, 
trong trường hợp này là df và tên nhiều tiêu đề cột được đặt trong dấu ngoặc kép. 
Kết quả được một khung dữ liệu mới bao gồm các cột được chỉ định:'''
# Access to multiple columns

y = df[['Artist','Length','Genre']]
print(y)

'''Một cách để truy cập các phần tử duy nhất là phương thức iloc, bạn có thể truy cập hàng đầu tiên và cột đầu tiên như sau:'''
# Access the value on the first row and the first column

print(df.iloc[0, 0])
'''Bạn có thể truy cập hàng thứ 2 và cột thứ nhất như sau:'''
# Access the value on the second row and the first column

print(df.iloc[1,0])
'''Bạn có thể truy cập hàng đầu tiên và cột thứ 3 như sau:'''
# Access the value on the first row and the third column

print(df.iloc[0,2])
'''Bạn cũng có thể truy cập cột bằng cách sử dụng tên, các mục sau giống như trên:'''
# Access the column using the name

df.loc[0, 'Artist']

# Access the column using the name

df.loc[1, 'Artist']
# Access the column using the name

df.loc[0, 'Released']
# Access the column using the name

df.loc[1, 'Released']
'''Bạn có thể thực hiện cắt bằng cách sử dụng cả chỉ mục và tên của cột:'''
# Slicing the dataframe

print(df.iloc[0:2, 0:3])

# Slicing the dataframe using name

print(df.loc[0:2, 'Artist':'Released'])

'''Quiz về Khung dữ liệu
Sử dụng biến q để lưu cột Rating dưới dạng khung dữ liệu

'''
# Write your code below and press Shift+Enter to execute
q = df['Rating']

'''Gán biến q cho khung dữ liệu được tạo thành từ cột Released và Artist:'''
# Write your code below and press Shift+Enter to execute
q = df[['Released', 'Artist']]

'''Truy cập hàng thứ 2 và cột thứ 3 của df:'''
# Write your code below and press Shift+Enter to execute
df.iloc[1,4]