'''Ta có thể mở một đối tượng tệp sử dụng phương thức write() để lưu tệp văn bản ra một danh sách. 
Để viết mode, đối số phải được thiết lập để ghi w. Hãy ghi tệp Example2.txt với dòng: “This is line A”'''
# Write line to file
exmp2 ='Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
'''Ta có thể đọc tệp xem nó có hoạt động không'''
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

'''Ta có thể đọc nhiều dòng'''
# Write lines to file

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

'''Bạn có thể kiểm tra tệp tin xem kết quả của bạn có chính xác không'''# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

'''Chúng ta ghi danh sách vào tệp .txt như sau:'''
# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
'''Chúng ta có thể xác thực tệp được viết bằng cách đọc và in ra các giá trị:'''

# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

'''Tuy nhiên, lưu ý rằng việc đặt mode thành w sẽ ghi đè lên tất cả dữ liệu hiện có trong tệp.'''
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

'''Ghi thêm tệp tin (Appending Files)
Chúng ta có thể ghi vào tệp mà không làm mất bất kỳ dữ liệu hiện có nào như sau bằng cách đặt đối số mode thành append a. 
Bạn có thể thêm một dòng mới như sau:'''
# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
'''Bạn có thể xác thực tệp đã thay đổi bằng cách chạy ô sau:'''
# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
'''Các mode khác
Việc mở tệp bằng a hoặc w và sau đó mở lại trong r để đọc bất kỳ dòng nào khá là không hiệu quả. 
May mắn thay, chúng ta có thể truy cập tệp ở các mode sau:

r+ Đọc và ghi. Không thể cắt ngắn tệp.
w+ : Ghi và đọc. Cắt bớt tệp.
a+ : Ghi thêm và Đọc. Tạo một tệp mới, nếu không có tệp nào tồn tại. 
Bạn không cần phải tìm hiểu chi tiết cụ thể của từng mode cho lab này.
Hãy thử mode a+:'''
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
'''Không có lỗi nhưng read() cũng không xuất ra bất kỳ thứ gì. Điều này là do vị trí của chúng ta trong tệp.

Hầu hết các phương thức tệp mà chúng ta đã xem đều hoạt động ở một vị trí nhất định trong tệp. 
.write() ghi tại một vị trí nhất định trong tệp. 
.read() đọc tại một vị trí nhất định trong tệp, v.v. 
Bạn có thể coi điều này giống như việc di chuyển con trỏ của bạn trong sổ ghi chú để thực hiện các thay đổi tại vị trí cụ thể.

Mở tệp trong w cũng giống như mở tệp .txt, di chuyển con trỏ của bạn đến đầu tệp văn bản, 
viết văn bản mới và xóa mọi thứ sau đó. Trong khi đó, việc mở tệp bằng a tương tự như mở tệp .txt, 
di chuyển con trỏ của bạn đến cuối và sau đó thêm các đoạn văn bản mới.
Thường rất hữu ích khi biết vị trí của 'cursor' (con trỏ) trong tệp và có thể kiểm soát nó. 
Các phương pháp sau đây cho phép chúng ta thực hiện chính xác điều này -

.tell() - trả về vị trí hiện tại tính bằng byte
.seek(offset,from) - thay đổi vị trí của byte 'offset' đối với 'from'. 
From có thể lấy giá trị 0,1,2 tương ứng với phần đầu, liên quan đến vị trí hiện tại và kết thúc
Bây giờ ta hãy quay lại với a+'''
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

'''Cuối cùng, một lưu ý về sự khác biệt giữa w+ và r+. Cả hai mode này đều cho phép truy cập các phương thức đọc và ghi. 
Tuy nhiên, việc mở tệp trong w+ sẽ ghi đè tệp đó và xóa tất cả dữ liệu hiện có.
Để làm việc với tệp trên dữ liệu hiện có, hãy sử dụng r+ và a+. 
Trong khi sử dụng r+, bạn nên thêm phương thức .truncate() vào cuối dữ liệu của bạn. 
Điều này sẽ giảm tệp dữ liệu của bạn và xóa mọi thứ đi cùng phần giảm đó.
Trong khối code sau, Chạy code như lúc đầu và sau đó chạy nó với .truncate().'''
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

'''Sao chép một tệp tin
Hãy sao chép tệp Example2.txt vào tệp Example3.txt:

'''
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
'''Ta có thể đọc tệp tin để xem mọi thứ có hoạt động không:'''
# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())

'''Sau khi đọc tệp, chúng ta cũng có thể ghi dữ liệu vào tệp và lưu chúng ở các định dạng tệp khác nhau như
 .txt, .csv, .xls (đối với tệp excel), v.v.. Bạn sẽ gặp những định dàng này trong các ví dụ khác

Bây giờ hãy chuyển đến thư mục để đảm bảo tệp .txt tồn tại và chứa dữ liệu tóm tắt mà chúng ta đã viết.'''

'''Exercise
Câu lạc bộ người hâm mộ Raptors của trường đại học địa phương của bạn duy trì danh sách các thành viên tích cực 
của mình trên tài liệu .txt. Hàng tháng, họ cập nhật tệp bằng cách loại bỏ các thành viên không hoạt động. 
Bạn đã được giao nhiệm vụ tự động hóa điều này bằng các kỹ năng python của mình.
Với tệp currentMem, loại từng thành viên có 'no' trong cột không hoạt động của họ. 
Theo dõi từng thành viên đã bị loại bỏ và thêm họ vào tệp exMem. Đảm bảo định dạng của tệp gốc được giữ nguyên. 
(Gợi ý: Làm điều này bằng cách đọc/ghi toàn bộ dòng và đảm bảo vẫn giữ nguyên tiêu đề)
Chạy khối code bên dưới trước khi bắt đầu exercise. Khung code đã cung cấp cho bạn, bạn chỉ chỉnh sửa hàm cleanFiles.'''
