# -*- coding: utf-8 -*-
"""[VN]Lab_7_1_Viết code Python đầu tiên của bạn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F6u-oKdaf0PVHKUXdr4O9WLwMWDzCq7d

#Lab 7.1  Viết code Python đầu tiên của bạn

Thời lượng ước tính: **25** phút

## Mục tiêu

Sau khi hoàn thành lab này, bạn sẽ có thể:

-   Viết code cơ bản trong Python
-   Làm việc với các loại dữ liệu khác nhau trong Python
-   Chuyển đổi dữ liệu từ dạng này sang dạng khác
-   Sử dụng các biểu thức và biến để thực hiện các phép toán

<h2>Mục lục</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>
            <a href="#hello">Nói "Hello" trong Python</a>
            <ul>
                <li><a href="version">Bạn đang dùng Python phiên bản nào?</a></li>
                <li><a href="comments">Viết comment (chú dẫn) trong Python</a></li>
                <li><a href="errors">Các lỗi trong Python</a></li>
                <li><a href="python_error">Liệu Python có phát hiện lỗi trước khi chạy code của bạn?</a></li>
                <li><a href="exercise">Exercise: Chương trình đầu tiên của bạn</a></li>
            </ul>
        </li>
        <li>
            <a href="#types_objects">Các kiểu đối tượng trong Python</a>
            <ul>
                <li><a href="int">Số nguyên</a></li>
                <li><a href="float">Số thực</a></li>
                <li><a href="convert">Chuyển đổi đối tượng từ một kiểu này sang kiểu khác</a></li>
                <li><a href="bool">Kiểu dữ liệu Boolean</a></li>
                <li><a href="exer_type">Exercise: Các kiểu dữ liệu</a></li>
            </ul>
        </li>
        <li>
            <a href="#expressions">Biểu thức và biến</a>
            <ul>
                <li><a href="exp">Biểu thức</a></li>
                <li><a href="exer_exp">Exercise: Biểu thức</a></li>
                <li><a href="var">Biến</a></li>
                <li><a href="exer_exp_var">Exercise: Biểu thức và biến trong Python</a></li>
            </ul>
        </li>
    </ul>
    <p>
        Thời lượng ước tính cần thiết: <strong>25 phút</strong>
    </p>
</div>

<hr>

<h2 id="hello">Nói "Hello" trong Python</h2>

Khi học một ngôn ngữ lập trình mới, thông thường bạn nên bắt đầu với một ví dụ "hello world". Nói một cách đơn giản, dòng code này sẽ đảm bảo cho chúng ta biết cách in một chuỗi ở đầu ra và cách thực thi code trong các ô trong notebook.

<hr/>
<div class="alert alert-success alertsuccess" style="margin-top: 20px">
[Tip]: Để thực thi code Python trong ô dưới đây, bấm vào ô để chọn và ấn <kbd>Shift</kbd> + <kbd>Enter</kbd>.
</div>
<hr/>
"""

# Try your first Python output

print('Hello, Python!')

"""Sau khi thực hiện ô trên, bạn sẽ thấy Python in ra <code>Hello, Python!</code>. Chúc mừng bạn đã chạy code Python đầu tiên của mình!

<hr/>
<div class="alert alert-success alertsuccess" style="margin-top: 20px">
    [Tip:] <code>print()</code> là một hàm. Bạn truyền chuỗi <code>'Hello, Python!'</code> như một đối số để hướng dẫn Python thứ cần in.
</div>
<hr/>

<h3 id="version">Bạn đang dùng Python bản nào?</h3>

<p>
    Có hai phiên bản phổ biến của ngôn ngữ lập trình Python được sử dụng hiện nay: Python 2 và Python 3. Cộng đồng Python đã quyết định chuyển từ Python 2 sang Python 3 và nhiều thư viện phổ biến đã thông báo rằng họ sẽ không hỗ trợ Python 2 nữa.
</p>
<p>
    Vì Python 3 có tương lai nên trong khóa học này, chúng tôi sẽ chỉ sử dụng nó. Làm cách nào để biết rằng notebook của chúng ta được thực thi bởi runtime Python 3? Chúng ta có thể nhìn vào góc trên bên phải của notebook này và thấy "Python 3".
</p>
<p>
    Chúng ta cũng có thể hỏi trực tiếp Python và nhận được câu trả lời chi tiết. Hãy thử thực hiện code sau:
</p>
"""

# Check the Python Version

import sys
print(sys.version)

"""<hr/>
<div class="alert alert-success alertsuccess" style="margin-top: 20px">
    [Tip:] <code>sys</code> là một mô-đun tích hợp chứa nhiều hàm hoặc tham số dành riêng cho hệ thống, bao gồm phiên bản Python đang dùng. Trước khi dùng, chúng ta phải <code>import</code> (nhập) nó rõ ràng.
</div>
<hr/>

<h3 id="comments">Viết comments trong Python</h3>

<p>
   Ngoài việc viết code, hãy lưu ý rằng bạn luôn nên thêm comment vào code của mình. Nó sẽ giúp người khác hiểu những gì bạn đang cố gắng hoàn thành (lý do tại sao bạn viết một đoạn code nhất định). Điều này không chỉ giúp <strong> người khác </strong> hiểu code của bạn mà còn có thể đóng vai trò như một lời nhắc nhở <strong> cho bạn </strong> khi quay lại code này sau vài tuần hoặc vài tháng.</p>

<p>
    Để viết comment trong Python, hãy sử dụng ký hiệu số <code> # </code> trước khi viết comment. Khi bạn chạy code, Python sẽ bỏ qua mọi thứ sau <code> # </code> trên một dòng nhất định.
</p>
"""

# Practice on writing comments

print('Hello, Python!') # This line prints a string
# print('Hi')

"""<p>
    Sau khi thực thi ô ở trên, bạn sẽ nhận thấy rằng <code> This line prints a string </code> không xuất hiện ở đầu ra, vì đó là một comment (và do đó bị Python bỏ qua).
</p>
<p>
    Dòng thứ hai cũng không được thực thi vì <code> print ('Hi') </code> đứng sau kí hiệu (<code> # </code>)! Vì đây không phải là một comment giải thích từ lập trình viên, mà là một dòng code thực tế, chúng ta có thể nói rằng lập trình viên đã <em> ghi chú </em> dòng code thứ hai đó.
</p>

<h3 id="errors">Các lỗi trong Python</h3>

<p>Ai cũng mắc sai lầm. Đối với nhiều loại lỗi, Python sẽ cho bạn biết rằng bạn đã mắc lỗi bằng cách đưa ra một thông báo lỗi. Điều quan trọng là phải đọc kỹ các thông báo này để thực sự hiểu bạn đã mắc lỗi ở đâu và cách sửa.</p>
<p>Ví dụ, nêu bạn viết <code>print</code> thành <code>frint</code>, Python sẽ hiển thị thông báo lỗi. Hãy thử:</p>
"""

# Print string as error message

frint("Hello, Python!")

"""<p>Thông báo lỗi cho bạn biết: 
<ol>
    <li>nơi xảy ra lỗi (sẽ hữu ích hơn trong các ô notebook hoặc tập lệnh lớn hơn), và</li> 
    <li>đó là loại lỗi nào (NameError)</li> 
</ol>
<p>Ở đây, Python cố gắng chạy hàm <code>frint</code>, nhưng không thể xác định <code>frint</code> là gì vì nó không phải hàm tích hợp hoặc trước đó chúng ta cũng không xác đinh.</p>

<p>
    Bạn sẽ nhận thấy rằng nếu chúng ta mắc một loại lỗi khác do quên đóng chuỗi, sẽ gặp một lỗi khác (ví dụ: <code>SyntaxError</code>). Hãy thử dưới đây :
</p>
"""

# Try to see build in error message

print("Hello, Python!)

"""<h3 id="python_error">Python có phát hiện lỗi trước khi bạn chạy code của mình không?</h3>

Python được coi là một <em> ngôn ngữ thông dịch </em>. Các ngôn ngữ biên dịch sẽ kiểm tra toàn bộ chương trình của bạn tại thời điểm biên dịch và có thể cảnh báo bạn về toàn bộ lớp lỗi trước khi thực thi. Ngược lại, Python diễn giải từng dòng tập lệnh của bạn khi nó thực thi. Python sẽ ngừng thực thi toàn bộ chương trình khi nó gặp lỗi (trừ khi lỗi được lập trình viên dự kiến và xử lý, một chủ đề nâng cao hơn mà chúng ta sẽ đề cập sau trong khóa học này).

Hãy thử chạy đoạn code trong ô bên dưới và xem điều gì sẽ xảy ra:
"""

# Print string and error to see the running order

print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")

"""<h3 id="exercise">Exercise: Chương trình đầu tiên của bạn</h3>

<p>Các thế hệ lập trình viên bắt đầu sự nghiệp lập trình đơn giản bằng việc in ra"Hello, world!". Bạn hãy học tập họ. </p>
<p>Trong ô code dưới đây, hãy dùng hàm <code>print()</code> để in ra đoạn sau: <code>Hello, world!</code></p>
"""

# Viết code của bạn ở dưới. Đừng quên ấn Shift+Enter để chạy ô
print ("Hello, world!")

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
print("Hello, world!")

```

</details>

<p>Giờ hãy tăng cường code của bạn với một comment. Trong ô code dưới đây, hãy in ra cụm: <code>Hello, world!</code> và chú thích với cụm <code>Print the traditional hello world</code> tất cả trong một dòng code.</p>
"""

# Viết code của bạn ở dưới. Đừng quên ấn Shift+Enter để chạy ô
print('Hello, world!') # Print traditional hello world

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
print("Hello, world!") # Print the traditional hello world

```

</details>

<hr>

<h2 id="types_objects" align="center">Các kiểu đối tượng trong Python</h2>

<p>Python là một ngôn ngữ hướng đối tượng. Có nhiều kiểu đối tượng trong Python. Hãy bắt đầu với những kiểu phổ biến nhất: <i>chuỗi (string)</i>, <i>số nguyên (integer)</i> và <i>số thực (float)</i>. Bất cứ khi nào bạn viết từ (văn bản) trong Python, tức là bạn đang dùng <i>chuỗi kí tự</i> (gọi ngắn gọn là chuỗi). Ngược lại, các kiểu số phổ biến nhất là <i>số nguyên</i> (ví dụ: -1, 0, 100) và <i>số thực</i>, biểu thị các số thực (ví dụ: 3.14, -42.0).</p>

<a align="center">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesObjects.png" width="600">
</a>

<p>Các ô code sau đây chứa một số ví dụ.</p>
"""

# Integer

11

# Float

2.14

# String

"Hello, Python 101!"

"""<p>Bạn có thể yêu cầu Python cho bạn biết loại biểu thức bằng cách sử dụng hàm <code>type()</code> tích hợp sẵn. Bạn sẽ nhận thấy rằng Python đề cập đến các số nguyên dưới dạng <code>int</code>, số thực ở dạng <code>float</code>, và chuỗi kí tự ở dạng <code>str</code>.</p>

"""

# Type of 12

type(12)

# Type of 2.14

type(2.14)

# Type of "Hello, Python 101!"

type("Hello, Python 101!")

"""<p>Trong ô code bên dưới, hãy dùng hàm <code>type()</code> để xem kiểu đối tượng của <code>12.0</code>.

"""

# Viết code của bạn ở dưới. Đừng quên ấn Shift+Enter để chạy ô
type(12.0)

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
type(12.0)

```

</details>

<h3 id="int">Số nguyên</h3>

<p>Dưới đây là một số ví dụ về số nguyên. Số nguyên có thể là số nguyên âm hoặc nguyên dương:</p>

<a align="center">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesInt.png" width="600">
</a>

<p>Bạn có thể xác thực bằng cách dùng hàm <code>type()</code>:
"""

# Print the type of -1

type(-1)

# Print the type of 4

type(4)

# Print the type of 0

type(0)

"""<h3 id="float">Số thực</h3>

<p>Số thực là một tập hợp các số nguyên nhưng cũng bao gồm "các số thập phân". Có một số hạn chế khi nói đến máy biểu diễn số thực, nhưng số dấu phẩy động là điển hình trong hầu hết các trường hợp. Bạn có thể tìm hiểu thêm về các chi tiết cụ thể của số thực cho môi trường runtime của mình bằng cách kiểm tra giá trị của <code> sys.float_info </code>. Điều này cũng sẽ cho bạn biết số lớn nhất và số nhỏ nhất có thể được chúng biểu thị.</p>

<p>Một lần nữa, các bạn có thể kiểm tra một số ví dụ với hàm <code>type()</code>:
"""

# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float

# Print the type of 0.5

type(0.5)

# Print the type of 0.56

type(0.56)

# System settings about float type

sys.float_info

"""<h3 id="convert">Chuyển đổi một đối tượng từ kiểu này sang kiểu khác</h3>

<p>Bạn có thể đổi kiểu đối tượng trong Python (ép kiểu). Ví dụ, bạn có thể chuyển một <i>số nguyên</i> thành một <i>số thực</i> (ví dụ: 2 thành 2.0).</p>
<p>Hãy thử:</p>
"""

# Verify that this is an integer

type(2)

"""<h4>Chuyển số nguyên thành số thực</h4>
<p>Hãy chuyển số nguyên 2 thành số thực:</p>

"""

# Convert 2 to a float

float(2)

# Convert integer 2 to a float and check its type

type(float(2))

"""<p>Khi chuyển đổi số nguyên thành số thực, chúng ta không thực sự thay đổi giá trị. Tuy nhiên, nếu chuyển từ số thực thành số nguyên, chúng ta có thể mất một số thông tin. Chẳng hạn, nếu chuyển từ số thực 1.1 thành số nguyên 1 thì sẽ mất thông tin phần thập phân (0.1):</p>

"""

# Casting 1.1 to integer will result in loss of information

int(1.1)

"""<h4>Chuyển từ chuỗi thành số nguyên hoặc số thực</h4>

<p>Đôi lúc, bạn sẽ có một chuỗi chứa một số trong đó. Trong trường hợp này, chúng ta có thể ép chuỗi đó thể hiện một số thành một số nguyên sử dụng <code>int()</code>:</p>
"""

# Convert a string into an integer

int('1')

"""<p>Nhưng nếu bạn cố gắng làm như vậy với một chuỗi không cho kết quả khớp hoàn hảo cho một số, bạn sẽ gặp lỗi. Hãy thử những cách sau:</p>

"""

# Convert a string into an integer with error

int('1 or 2 people')

"""<p>Bạn cũng có thể chuyển chuỗi có chứa số dấu phẩy động thành đối tượng <i>float</i> :</p>

"""

# Convert the string "1.2" into a float

float('1.2')

"""<hr/>
<div class="alert alert-success alertsuccess" style="margin-top: 20px">
    [Tip:] Lưu ý rằng các chuỗi có thể được biểu diễn bằng dấu nháy đơn (<code> '1.2' </code>) hoặc dấu nháy kép (<code> "1.2" </code>), nhưng bạn không thể kết hợp cả hai (ví dụ: <code> "1.2'</code>).
</div>
<hr/>

<h4>Chuyển số thành chuỗi</h4>

<p>Nếu chúng ta có thể chuyển đổi chuỗi thành số, thì việc chúng ta có thể chuyển đổi số thành chuỗi là điều đương nhiên phải không?</p>
"""

# Convert an integer to a string

str(1)

"""<p>Và không có lý do gì chúng ta không thể chuyển số thực thành chuỗi:</p> 

"""

# Convert a float to a string

str(1.2)

"""<h3 id="bool">Kiểu dữ liệu Boolean</h3>

<p><i>Boolean</i> là một kiểu quan trọng khác trong Python. Đối tượng của kiểu  <i>Boolean</i> có thể lấy một trong 2 giá trị: <code>True</code> hoặc <code>False</code>:</p>
"""

# Value true

True

"""<p>Lưu ý rằng gái trị <code>True</code> có chữ "T" viết hao. <code>False</code> cũng vậy (bạn phải viết hoa chữ "F").</p>

"""

# Value false

False

"""<p>Khi bạn yêu cầu Python hiển thị kiểu đối tượng Boolean, nó sẽ hiển thị <code>bool</code> thay vì <i>boolean</i>:</p> 

"""

# Type of True

type(True)

# Type of False

type(False)

"""<p>Chúng ta có thể ép kiểu các đối tượng boolean thành các kiểu dữ liệu khác. Nếu chúng ta ép kiểu boolean có giá trị <code>True</code> thành một số nguyên hoặc số thực, chúng ta sẽ nhận được 1. Nếu chúng ta ép kiểu boolean có giá trị <code>False</code> thành một số nguyên hoặc số thực, chúng ta sẽ nhận được 0. Tương tự, nếu ta chuyển 1 thành Boolean, bạn sẽ nhận được <code>True</code>. Và nếu chúng ta chuyển 0 thành Boolean sẽ nhận được <code>False</code>. Hãy thử:</p> 

"""

# Convert True to int

int(True)

# Convert 1 to boolean

bool(1)

# Convert 0 to boolean

bool(0)

# Convert True to float

float(True)

"""<h3 id="exer_type">Exercise: Các kiểu</h3>

<p>Kiểu dữ liệu của kết quả: <code>6 / 2</code> là?</p>
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
float(6/2)

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
type(6/2) # float

```

</details>

<p>Kiểu của kết quả: <code>6 // 2</code> là? (Chú ý dấu <code>//</code>.)</p>
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
int(6//2)

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
type(6//2) # int, as the double slashes stand for integer division 

```

</details>

<hr>

<h2 id="expressions">Biểu thức và biến</h2>

<h3 id="exp">Biểu thức</h3>

<p>Các biểu thức trong Python có thể bao gồm các phép toán giữa các kiểu tương thích (ví dụ: số nguyên và số thực). Chẳng hạn, các phép toán số học cơ bản như cộng nhiều số:</p>
"""

# Addition operation expression

43 + 60 + 16 + 41

"""<p>Chúng ta có thể thực hiện các phép tính trừ bằng toán tử trừ. Trong trường hợp này, kết quả là một số âm:</p>

"""

# Subtraction operation expression

50 - 60

"""<p>Chúng ta có thể thực hiện phép nhân với dấu hoa thị:</p>

"""

# Multiplication operation expression

5 * 5

"""<p>Chúng ta có thể thực hiện phép chia với dấu gạch chéo:

"""

# Division operation expression

25 / 5

# Division operation expression

25 / 6

"""<p>Như đã thấy trong quiz trên, chúng ta có thể dùng dấu gạch chéo kép để chia số nguyên, trong đó, kết quả được làm tròn đến số nguyên gần nhất:

"""

# Integer division operation expression

25 // 5

# Integer division operation expression

25 // 6

"""<h3 id="exer_exp">Exercise: Biểu thức</h3>

<p> Hãy viết biểu thức tính số giờ trong 160 phút:
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
160/60

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
160/60 

# Or 

160//60

```

</details>

<p>Python tuân theo các quy ước toán học được chấp nhận rộng rãi khi đánh giá các biểu thức toán học. Trong ví dụ sau, Python thêm 30 vào kết quả của phép nhân (tức là 120).
"""

# Mathematical expression

30 + 2 * 60

"""<p>Và theo toán học, các biểu thức đặt trong dấu ngoặc đơn được ưu tiên. Vì vậy, sẽ là 32 nhân với 60.

"""

# Mathematical expression

(30 + 2) * 60

"""<h3 id="var">Biến</h3>

<p>Cũng như hầu hết các ngôn ngữ lập trình, chúng ta có thể lưu trữ các giá trị trong <i> các biến </i>, để chúng ta có thể sử dụng chúng sau này. Ví dụ:</p>
"""

# Store value into variable

x = 43 + 60 + 16 + 41

"""<p>Để xem giá trị của <code>x</code> trong Notebook, bạn chỉ cần đặt nó ở dòng cuối của ô:</p>

"""

# Print out the value in variable

x

"""<p>Bạn cũng có thể thực hiện các phép toán với <code>x</code> và lưu kết quả vào một biến mới:</p>

"""

# Use another variable to store the result of the operation between variable and value

y = x / 60
y

"""<p>Nếu lưu một giá trị vào biến hiện có, giá trị mới sẽ được ghi đè lên giá trị trước đó:</p>

"""

# Overwrite variable with new value

x = x / 60
x

"""<p>Một phương pháp hay là sử dụng tên biến có ý nghĩa để bạn và những người khác có thể đọc và hiểu code dễ dàng hơn:</p>

"""

# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min

# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours 
total_hours

"""<p>Trong các ô ở trên, chúng ta đã thêm độ dài của ba album tính bằng phút và lưu trữ nó trong <code>total_min</code>. Sau đó, chia nó cho 60 để tính tổng độ dài<code>total_hours</code>theo giờ. Bạn cũng có thể thực hiện tất cả cùng một lúc trong một biểu thức, miễn là bạn sử dụng dấu ngoặc đơn để thêm độ dài album trước khi chia, như được hiển thị bên dưới.</p>

"""

# Complicate expression

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours

"""<p>Nếu bạn muốn có tổng số giờ là một số nguyên, bạn có thể thay thế phép chia dấu phẩy động bằng phép chia số nguyên (tức là <code>//</code>).</p>

<h3 id="exer_exp_var">Exercise: Biểu thức và Biến trong Python</h3>

<p>Giá trị của <code>x</code> là gì trong <code>x = 3 + 2 * 2</code>?</p>
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
x = 3 + 2 * 2
x

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
7

```

</details>

<p>Giá trị của <code>y</code> là gì trong <code>y = (3 + 2) * 2</code>?</p>
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
y = (3 + 2) * 2
y

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
10

```

</details>

<p>Giá trị của<code>z</code> là gì trong <code>z = x + y</code>?</p>
"""

# Write your code below. Don't forget to press Shift+Enter to execute the cell
z = x + y
z

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
17

```

</details>

<hr>
<p>Nguồn: IBM
<hr>
"""