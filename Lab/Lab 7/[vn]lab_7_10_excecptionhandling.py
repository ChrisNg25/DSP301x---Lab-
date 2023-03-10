# -*- coding: utf-8 -*-
"""[VN]Lab_7_10_ExcecptionHandling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O0Qm0bjlaNtJjjJHS39E9l0OBCe1YygE

# **Lab 7.10 Xử Lý Ngoại Lệ**

Thời gian ước tính cần thiết: **15** phút

## Mục tiêu

Sau khi hoàn thành lab này, bạn sẽ có thể:

* Hiểu các trường hợp ngoại lệ
* Xử lý các trường hợp ngoại lệ

## Mục Lục

* Ngoại lệ là gì?
* Xử lý ngoại lệ

***

## Ngoại lệ là gì ?

Trong phần này, bạn sẽ tìm hiểu về ngoại lệ là gì và là ví dụ về chúng.

### Định nghĩa

Ngoại lệ (exception) là một lỗi xảy ra trong quá trình thực thi code. Lỗi này khiến code tạo ra một ngoại lệ, và nếu không được chuẩn bị để xử lý nó sẽ tạm dừng việc thực thi code.

### Ví dụ

Chạy từng đoạn code và quan sát ngoại lệ được nêu.
"""

1/0

"""<code>ZeroDivisionError</code> xảy ra khi bạn cố chia cho 0.

"""

y = a + 5

"""<code>NameError</code> -- trong trường hợp này, điều đó có nghĩa là bạn đã cố gắng sử dụng biến a khi nó chưa được định nghĩa.

"""

a = [1, 2, 3]
a[10]

"""<code>IndexError</code> -- trong trường hợp này, nó xảy ra vì bạn đã cố truy cập dữ liệu từ list bằng cách sử dụng một index không tồn tại cho list này.

Có nhiều ngoại lệ khác được tích hợp trong Python, đây là danh sách các ngoại lệ: [https://docs.python.org/3/library/exceptions.html](https://docs.python.org/3/library/exceptions.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01)

## Xử lý ngoại lệ

Ở phần này, chúng ta sẽ học cách xử lý các ngoại lệ. Bạn sẽ hiểu cách khiến chương trình thực hiện các tác vụ được chỉ định thay vì tạm dừng thực thi code khi gặp ngoại lệ.

### Try Except

<code>try except</code> sẽ cho phép bạn thực thi code có thể tạo ra ngoại lệ và trong trường hợp có một ngoại lệ bất kỳ hoặc một ngoại lệ cụ thể nào, chúng ta có thể xử lý hoặc phát hiện các ngoại lệ và thực thi code cụ thể. Điều này sẽ cho phép chúng ta tiếp tục thực hiện chương trình của mình ngay cả khi có ngoại lệ.

Python cố gắng thực thi code trong <code>try</code> block. Trong trường hợp này, nếu có bất kỳ ngoại lệ nào mà code trong khối <code>try</code> đưa ra, nó sẽ bị phát hiện và khối code trong <code>except</code> block sẽ được thực thi. Sau đó, code xuất hiện <em>sau</em> try except sẽ được thực thi.
"""

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except:
    # code để thực thi nếu có ngoại lệ
    
# code vẫn sẽ thực thi nếu có ngoại lệ

"""### Ví dụ về Try Except

Trong ví dụ này, chúng ta đang cố gắng chia một số mà người dùng cung cấp, lưu kết quả trong biến <code>a</code>, sau đó in kết quả của phép toán. Khi lấy dữ liệu đầu vào của người dùng và chia một số cho nó, có thể sẽ xuất hiện một số ngoại lệ, chẳng hạn như khi chúng ta chia cho 0. Hãy thử chạy khối code sau với <code>b</code> là một số. Ngoại lệ sẽ chỉ xuất hiện nếu <code>b</code> bằng 0.
"""

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")

"""### Try Except đặc trưng

<code>try except</code> đặc trưng cho phép chúng ta nắm bắt một số ngoại lệ nhất định, đồng thời thực thi một số code nhất định, tùy thuộc vào ngoại lệ. Điều này rất hữu ích nếu bạn không muốn xử lý một số ngoại lệ và việc thực thi sẽ tạm dừng. Nó cũng có thể giúp bạn tìm ra các lỗi trong code của mình mà bạn không nhận thấy. Hơn nữa, nó có thể giúp bạn phân biệt response đối với các ngoại lệ khác nhau. Trong trường hợp này, code sau try except có thể không chạy tùy thuộc vào lỗi.

<b>Các cell sau chỉ để minh họa, không chạy:</b>
"""

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except (ZeroDivisionError, NameError):
    # code để thử thực thi nếu có ngoại lệ thuộc các kiểu đã cho
    
# code sẽ thực thi nếu không có ngoại lệ hoặc có ngoại lệ mà chúng ta đang xử lý

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except ZeroDivisionError:
    # code để thử thực thi nếu có ZeroDivisionError
except NameError:
    # code để thử thực thi nếu có NameError
    
# code sẽ thực thi nếu không có ngoại lệ hoặc có ngoại lệ mà chúng ta đang xử lý

"""Cũng có thể có <code>except</code> rỗng ở cuối để phát hiện một ngoại lệ không mong muốn:

<b>Các cell sau chỉ để minh họa, không chạy:</b>
"""

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except ZeroDivisionError:
    # code để thử thực thi nếu có ZeroDivisionError
except NameError:
    # code để thử thực thi nếu có NameError
except:
    # code để thử thực thi nếu có bất kỳ ngoại lệ nào
    
# code sẽ thực thi nếu không có ngoại lệ hoặc có ngoại lệ mà chúng ta đang xử lý

"""### Ví dụ về Try Except đặc trưng

Ví dụ này tương tự như ở trên, nhưng bây giờ chúng ta sẽ thêm các message khác tùy thuộc vào ngoại lệ, cho người dùng biết đầu vào có vấn đề gì.
"""

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

"""### Try Except Else và Finally

<code>else</code> cho phép kiểm tra xem có ngoại lệ nào không khi thực hiện try block. Điều này rất hữu ích khi chúng ta chỉ muốn thực thi một điều gì đó mà không có lỗi.

<b>Các cell sau chỉ để minh họa, không chạy:</b>
"""

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except ZeroDivisionError:
    # code để thử thực thi nếu có ZeroDivisionError
except NameError:
    # code để thử thực thi nếu có NameError
except:
    # code để thử thực thi nếu có bất kỳ ngoại lệ nào
else:
    # code để thử thực thi nếu không có ngoại lệ
    
# code sẽ thực thi nếu không có ngoại lệ hoặc có ngoại lệ mà chúng ta đang xử lý

"""<code>finally</code> cho phép chúng ta luôn thực thi một thứ gì đó dù có ngoại lệ hoặc không. Nó thường được sử dụng để biểu thị sự kết thúc của try except.

"""

# những code tiềm năng trước khi thử catch

try:
    # code để thử thực thi
except ZeroDivisionError:
    # code để thử thực thi nếu có ZeroDivisionError
except NameError:
    # code để thử thực thi nếu có NameError
except:
    # code để thử thực thi nếu có bất kỳ ngoại lệ nào
else:
    # code để thử thực thi nếu không có ngoại lệ
finally:
    # code để thử thực thi ở cuối try except, bất kể code thế nào
    
# code sẽ thực thi nếu không có ngoại lệ hoặc có ngoại lệ mà chúng ta đang xử lý

"""### Ví dụ về Try Except Else và Finally

Bạn có thể nhận thấy rằng ngay cả khi có lỗi, giá trị <code>a</code> vẫn được in ra. Hãy sử dụng <code>else</code> và in giá trị của <code>a</code> chỉ khi không có lỗi.
"""

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

"""Bây giờ, hãy cho người dùng biết rằng chúng ta đã xử lý xong câu trả lời của họ. Sử dụng <code>finally</code>, hãy thêm một bản in.

"""

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

"""<hr>
Nguồn: IBM
<hr>

"""