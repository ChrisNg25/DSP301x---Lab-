# -*- coding: utf-8 -*-
"""[VN]Lab_7_9_Functions_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tlmwfzkvQK75yH4EfAH9nLMTdatmZW1b

#Lab 7.9 Hàm trong Python

Thời lượng ước tính: **40** phút

## Mục tiêu

Sau khi hoàn thành lab này, bạn sẽ có thể:

-   Hiểu về hàm và biến
-   Làm việc với hàm và biến

<h1>Hàm trong Python</h1>

<p><strong>Xin chào!</strong> Notebook này sẽ dạy bạn về các hàm trong Ngôn ngữ lập trình Python. Ở cuối lab này, bạn sẽ biết các khái niệm cơ bản về hàm, biến và cách sử dụng hàm.</p>

<h2>Mục lục</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>
            <a href="#func">Hàm</a>
            <ul>
                <li><a href="content">Hàm là gì?</a></li>
                <li><a href="var">Biến</a></li>
                <li><a href="simple">Hàm giúp đơn giản hóa mọi thứ</a></li>
            </ul>
        </li>
        <li><a href="pre">Hàm định nghĩa trước</a></li>
        <li><a href="if">Sử dụng câu lệnh <code>if</code>/<code>else</code> và Vòng lặp trong hàm</a></li>
        <li><a href="default">Thiết lập các giá trị đối số mặc định trong hàm tùy chỉnh</a></li>
        <li><a href="global">Biến toàn cục</a></li>
        <li><a href="scope">Phạm vi của biến</a></li>
        <li><a href="collec">Kiểu dữ liệu tập hợp và hàm</a></li>
        <li>
            <a href="#quiz">Quiz về Hàm</a>
        </li>
    </ul>

</div>

<hr>

<h2 id="func">Hàm</h2>

Hàm là một khối code có thể tái sử dụng để thực hiện các thao tác được chỉ định trong hàm. Chúng cho phép bạn chia nhỏ các tác vụ và sử dụng lại code của mình trong các chương trình khác nhau.

Có 2 kiểu hàm :

-   <b>Hàm định nghĩa trước (Pre-defined function)</b>
-   <b>Hàm do người dùng định nghĩa (User defined function)</b>

<h3 id="content">Hàm là gì?</h3>

Bạn có thể xác định các hàm để cung cấp chức năng cần thiết. Dưới đây là các quy tắc đơn giản để xác định một hàm trong Python:

-   Khối hàm bắt đầu với <code>def</code> theo sau là hàm <code>(tên hàm)</code> và dấu <code>()</code>.
-   Thay các tham số hoặc đối số vào trong dấu ngoặc đơn.
-   Bạn cũng có thể xác định các tham số bên trong dấu ngoặc đơn.
-   Sau dấu <code>:</code> là phần thân hàm và cần thụt lề.
-   You can also place documentation before the body. bạn cũng có thể đặt đoạn văn bản trước phần thân hàm.
-   Câu lệnh <code>return</code> thoát một hàm, tùy chọn trả về một giá trị.

Ví dụ, hàm thêm tham số <code> a</code> sẽ in và trả về đầu ra là <code> b</code>:
"""

# First function example: Add 1 to a and store as b

def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)

"""Hình sau mô tả thuật ngữ:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsDefinition.png" width="500" />

Bạn có thể tìm trợ giúp về hàm:
"""

# Get a help on add function

help(add)

"""Chúng ta có thể gọi hàm:

"""

# Call the function add()

add(1)

"""Nếu gọi hàm với đầu vào mới, chúng ta sẽ nhận được kết quả mới:"""

# Call the function add()

add(2)

"""Chúng ta có thể tạo các hàm khác nhau. Ví dụ, chúng ta có thể tạo một hàm để nhân hai số. Các số sẽ được thể hiện bằng các biến <code> a</code> và <code> b</code>:"""

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

"""Có thể dùng cùng một hàm cho các kiểu dữ liệu khác nhau. Chằng hạn, chúng ta có thể nhân 2 số nguyên:"""

# Use mult() multiply two integers

Mult(2, 3)

"""Lưu ý: cách hàm kết thúc với câu lệnh <code> return</code>, và trả lại một giá trị. Giá trị này có thể được gán thêm cho một biến khác như mong muốn.

<hr>
Cùng một hàm có thể được sử dụng cho các kiểu dữ liệu khác nhau. Ví dụ, chúng ta có thể nhân hai số nguyên:

2 số thực:
"""

# Use mult() multiply two floats

Mult(10.0, 3.14)

"""Bạn thậm chí có thể sao chép một string bằng cách nhân với một số nguyên:"""

# Use mult() multiply two different type values together

Mult(2, "Michael Jackson ")

"""<h3 id="var">Biến</h3>

Đầu vào cho một hàm được gọi là tham số hình thức.

Biến được khai báo trong một hàm được gọi là biến cục bộ. Tham số chỉ tồn tại trong hàm (tức là điểm mà hàm bắt đầu và dừng).

Biến được khai báo bên ngoài định nghĩa hàm là một biến toàn cục và giá trị của nó có thể truy cập và sửa đổi được trong suốt chương trình. Chúng ta sẽ thảo luận thêm về các biến toàn cục ở phần cuối của lab.
"""

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

"""Các nhãn được hiển thị trong hình:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsVar.png" width="500" />

Chúng ta có thể gọi hàm với đầu vào là <b> 3</b>:
"""

# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y

"""Chúng ta có thể gọi hàm với đầu vào là <b> 2</b> theo một cách khác:"""

# Directly enter a number as parameter

square(2)

"""Nếu không có câu lệnh <code> return</code>, hàm sẽ trả về <code> None</code>. Hai hàm sau là tương đương:"""

# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output

MJ()

# See the output

MJ1()

"""Việc in hàm sau khi gọi sẽ hiển thị câu lệnh trả về mặc định **None**:"""

# See what functions returns are

print(MJ())
print(MJ1())

"""Tạo hàm <code> con</code> nối hai string bằng phép toán cộng:"""

# Define the function for combining strings

def con(a, b):
    return(a + b)

# Test on the con() function

con("This ", "is")

"""<hr/>
    <div class="alert alert-success alertsuccess" style="margin-top: 20px">
        <h4> [Tip] Làm cách nào để tìm hiểu thêm về các hàm được định nghĩa trước trong Python? </h4>
        <p>Chúng tôi sẽ giới thiệu các hàm định nghĩa trước khi bạn tìm hiểu thêm về Python. Vì có quá nhiều hàm nên không có cách nào để dạy tất cả liền một lúc. Nhưng nếu bạn muốn xem qua, hãy tham khảo thẻ sau cho một số hàm định nghĩa trước thường được sử dụng: <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/Python_reference_sheet.pdf">Tham khảo</a></p>
    </div>
<hr/>

<h3 id="simple">Hàm giúp đơn giản hóa mọi thứ</h3>

Hãy xem xét hai dòng code trong <b> Block 1</b> và <b> Block 2</b>: quy trình cho mỗi khối là giống nhau. Điều duy nhất khác biệt là tên và giá trị biến.

<h4>Block 1:</h4>
"""

# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1

"""<h4>Block 2:</h4>

"""

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2

"""Chúng ta có thể thay thế các dòng code bằng một hàm. Hàm kết hợp nhiều lệnh thành một dòng code. Khi hàm được xác định, nó có thể được sử dụng nhiều lần. Bạn có thể gọi cùng một hàm nhiều lần trong chương trình của mình. Bạn có thể lưu hàm của mình và sử dụng nó trong một chương trình khác hoặc sử dụng hàm của người khác. Các dòng code trong code <b> Block 1 </b> và code <b> Block 2 </b> có thể được thay thế bằng hàm sau:"""

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)

"""Hàm này nhận hai đầu vào a và b, sau đó áp dụng một số phép toán để trả về c.
Chúng ta chỉ cần xác định hàm, thay thế các lệnh bằng hàm và nhập các giá trị mới của <code> a1</code>, <code> b1</code> và <code> a2</code>, <code> b2</code> làm đầu vào. Toàn bộ quá trình được thể hiện trong hình:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/images/FuncsPros.gif" width="850" />

Code **Blocks 1** và **Block 2** giờ có thể thay thế bằng code **Block 3** và code **Block 4**.

<h4>Block 3:</h4>
"""

a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1

"""<h4>Block 4:</h4>

"""

a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2

"""<hr>

<h2 id="pre">Hàm định nghĩa trước</h2>

Trong Python có rất nhiều hàm định nghĩa trước, hãy bắt đầu với những hàm đơn giản trước.

Hàm <code>print()</code>:
"""

# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

"""Hàm <code>sum()</code> cộng tất cả các phần tử trong một list hoặc tuple:"""

# Use sum() to add every element in a list or tuple together

sum(album_ratings)

"""Hàm <code>len()</code> trả về độ dài của list hoặc tuple: """

# Show the length of the list or tuple

len(album_ratings)

"""<h2 id="if">Sử dụng câu lệnh <code>if</code>/<code>else</code> và Vòng lặp trong hàm</h2>

Hàm <code> return()</code> đặc biệt hữu ích nếu hàm của bạn có bất kỳ câu lệnh IF nào khi bạn muốn đầu ra của mình phụ thuộc vào một số điều kiện:
"""

# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

"""Chúng ta có thể sử dụng vòng lặp trong hàm. Ví dụ: chúng ta có thể <code> in</code> ra từng phần tử trong list:"""

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])

"""<hr>

<h2 id="default">Thiết lập giá trị đối số mặc định trong các hàm tùy chỉnh</h2>

Bạn có thể đặt giá trị mặc định cho các đối số trong hàm của mình. Ví dụ: trong hàm <code>isGoodRating()</code>, điều gì sẽ xảy ra nếu chúng ta muốn tạo một ngưỡng cho những gì được coi là xếp hạng tốt? Có lẽ chúng ta nên có xếp hạng mặc định là 4:
"""

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input

isGoodRating()
isGoodRating(10)

"""<hr>

<h2 id="global">Biến toàn cục</h2>

Chúng ta đã tạo ra các biến bên trong các hàm, nhưng chưa thảo luận về các biến bên ngoài hàm. Chúng được gọi là các biến toàn cục.
<br>
Hãy thử xem <code> print1</code> trả về những gì:
"""

# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1)

"""<b>Chúng ta có Name Error:  <code>name 'internal_var' is not defined</code>. Tạo sao?</b>  

Đó là bởi vì tất cả các biến chúng ta tạo trong hàm là <b> biến cục bộ</b>, có nghĩa là việc gán biến không tồn tại bên ngoài hàm. 

Nhưng có một cách để tạo <b> biến toàn cục</b> từ bên trong một hàm như sau:

"""

artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

"""<h2 id="scope">Phạm vi của một biến</h2>

Phạm vi của một biến là một phần của chương trình mà biến đó có thể truy cập được. Các biến được khai báo bên ngoài tất cả các định nghĩa hàm, chẳng hạn như biến <code>myFavouriteBand</code> trong code hiển thị ở đây, có thể truy cập được từ bất kỳ đâu trong chương trình. Kết quả là, các biến như vậy được cho là có phạm vi toàn cục và được gọi là các biến toàn cục.
    <code>myFavouriteBand</code> là một biến toàn cục, vì vậy nó có thể truy cập được từ bên trong hàm <code>getBandRating</code> và chúng ta có thể sử dụng nó để xác định xếp hạng của một ban nhạc. Chúng ta cũng có thể sử dụng nó bên ngoài hàm, chẳng hạn như khi chuyển nó cho hàm print để hiển thị nó:
"""

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

"""Hãy xem phiên bản đã sửa code này của chúng ta. Bây giờ biến <code> myFavouriteBand</code> được xác định trong hàm <code> getBandRating</code>. Một biến được xác định trong một hàm được cho là một biến cục bộ của hàm đó. Điều đó có nghĩa là nó chỉ có thể truy cập được từ bên trong hàm mà nó được xác định. Hàm <code> getBandRating</code> của chúng ta sẽ vẫn hoạt động vì <code> myFavouriteBand</code> vẫn được xác định trong hàm. Tuy nhiên, chúng ta không thể in <code> myFavouriteBand</code> bên ngoài hàm nữa, vì nó là một biến cục bộ của hàm <code> getBandRating</code>; nó chỉ được xác định trong hàm <code> getBandRating</code>:"""

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

"""Cuối cùng, hãy xem ví dụ này. Bây giờ chúng ta có hai định nghĩa biến <code> myFavouriteBand</code>. Cái đầu tiên trong số này có phạm vi toàn cục và cái thứ hai là biến cục bộ trong hàm <code> getBandRating</code>. Trong hàm <code> getBandRating</code>, biến cục bộ được ưu tiên. **Deep Purple** sẽ được xếp hạng 10.0 khi được chuyển đến hàm <code> getBandRating</code>. Tuy nhiên, bên ngoài hàm <code> getBandRating</code>, biến cục bộ của <code> getBandRating</code> không được xác định, vì vậy biến <code> myFavouriteBand</code> mà chúng ta in là biến toàn cục, có giá trị là **AC/DC**:"""

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

"""<hr>
<h2 id ="collec">Kiểu dữ liệu tập hợp và hàm</h2>

Khi số lượng đối số cho một hàm không xác định, tất cả có thể được đóng gói thành một tuple như được hiển thị:
"""

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

"""Tương tự, các đối số cũng có thể được đóng gói vào một dictionary như được hiển thị:"""

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

"""Các hàm có thể cực kỳ mạnh mẽ và linh hoạt. Chúng có thể chấp nhận (và trả về) các kiểu dữ liệu, đối tượng và thậm chí cả các hàm khác dưới dạng đối số. Hãy xem xét ví dụ dưới đây:"""

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList

"""<hr>
Lưu ý cách các thay đổi được thực hiện đối với list không giới hạn trong phạm vi hàm. Điều này xảy ra vì nó là list **tham chiếu** được chuyển đến hàm - Bất kỳ thay đổi nào được thực hiện đều nằm ở phiên bản gốc của list. Do đó, mọi người nên thận trọng khi truyền các đối tượng có thể thay đổi vào các hàm.

<hr>

<h2>Quiz về Hàm</h2>

Hãy nghĩ ra một hàm để đầu vào thứ nhất chia cho đầu vào thứ hai:
"""

# Write your code below and press Shift+Enter to execute
a = int(input(" Nhập số nguyên: "))
b = int(input('Nhập số nguyên: '))
def division(a,b):
  if b != 0:
    return float(a/b)
  else:
    return 'Không thể chia'
division(a,b)

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
def div(a, b):
    return(a/b)
    
```

</details>

<hr>

Dùng hàm <code>con</code> cho câu hỏi sau.
"""

# Use the con function for the following question

def con(a, b):
    return(a + b)

"""Hàm <code> con</code> đã xác định trước đây có thể được sử dụng để cộng hai số nguyên hoặc chuỗi không?"""

# Write your code below and press Shift+Enter to execute
con(2,2)
con('2','2')

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
Yes, for example: 
con(2, 2)
    
```

</details>

<hr>

Hàm <code> con</code> đã xác định trước đây có thể được sử dụng để nối các list hoặc tuple không?
"""

# Write your code below and press Shift+Enter to execute
con([1,2,3],[4,5,6])

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
Yes, for example: 
con(['a', 1], ['b', 1])
    
```

</details>

<hr>
Nguồn: IBM
<hr>
"""