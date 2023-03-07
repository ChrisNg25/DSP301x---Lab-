example1 = "Example1.txt"
file1 = open(example1, "r")
# Print the path of file
print(file1.name)

'''Đối tượng tệp tin ở trong mode nào:'''
# Print the mode of file, either 'r' or 'w'

print(file1.mode)
'''Ta có thể đọc một tệp tin và gán nó với một biến:'''
FileContent = file1.read()
print(FileContent)

'''Tệp thuộc type string:'''
# Type of file content

print(type(FileContent))
'''Điều rất quan trọng là tệp cần được đóng khi kết thúc. 
Điều này giải phóng tài nguyên và đảm bảo tính nhất quán trên các phiên bản python khác nhau.'''
# Close file after finish

file1.close()

'''Cách tốt hơn để mở một tệp tin
Cách tốt hơn là sử dụng câu lệnh with, nó sẽ tự động đóng tệp ngay cả khi code gặp phải một ngoại lệ.
Code sẽ chạy mọi thứ trong khối thụt lề sau đó đóng đối tượng tệp.'''

# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

'''Đối tượng tệp đã bị đóng, bạn có thể xác minh nó bằng cách chạy ô sau:'''
# Verify if the file is closed

file1.closed
'''Chúng ta có thể thấy thông tin trong tệp tin:'''
# See the content of file

print(FileContent)

'''Khi phương thức .read(4) được gọi, 4 ký tự đầu tiên được gọi. Nếu chúng ta gọi lại phương thức, 4 ký tự tiếp theo sẽ được gọi. 
Đầu ra cho ô sau sẽ minh họa quy trình cho các đầu vào khác nhau cho phương thức read():'''
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

'''Dưới đây là một ví dụ sử dụng cùng một tệp, nhưng thay vào đó chúng ta đọc 16, 5 và 9 ký tự cùng một lúc:'''
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
'''Chúng ta cũng có thể đọc từng dòng của tệp bằng phương thức readline():'''
# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())
'''Chúng ta cũng có thể chuyển một đối số tới readline() để chỉ định số ký tự mà chúng ta muốn đọc. 
Tuy nhiên, không giống như read(), readline() chỉ có thể đọc tối đa một dòng.'''
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

'''Chúng ta có thể sử dụng một vòng lặp để lặp lại qua từng dòng:'''
# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

'''Chúng ta có thể sử dụng phương thức readlines() để lưu tệp văn bản vào danh sách:'''
# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
# Print the first line, second, third line

print(FileasList[0])
print(FileasList[1])
print(FileasList[2])
