# -*- coding: utf-8 -*-
"""[VN]Lab_7_3_List trong Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IW-i4_h738RRv_YzLPSwu9M0mOgPxJfP

# Lab 7.3 List trong  Python

Thời lượng ước tính: **15** phút

## Mục tiêu

Sau khi hoàn thành lab này, bạn sẽ có thể:

-   Thực hiện các thao tác với List (danh sách) trong Python, bao gồm chỉ mục, thao tác list và sao chép/tạo bản sao list.

<h2>Mục lục</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>
            <a href="#dataset">Về tập dữ liệu</a>
        </li>
        <li>
            <a href="#list">List</a>
            <ul>
                <li><a href="index">Chỉ mục</a></li>
                <li><a href="content">Nội dung list</a></li>
                <li><a href="op">Thao tác list</a></li>
                <li><a href="co">Sao chép và tạo bản sao list</a></li>
            </ul>
        </li>
        <li>
            <a href="#quiz">Quiz về List</a>
        </li>
    </ul>
   
</div>

<hr>

<h2 id="#dataset">Về tập dữ liệu</h2>

Hãy tưởng tượng bạn nhận được các đề xuất về album từ bạn bè và tổng hợp tất cả các gợi ý vào một bảng, với thông tin cụ thể về từng album.

Trong bảng, thông tin mỗi bộ phim nằm trong một hàng và các cột:

-   **artist** - Tên nghệ sĩ
-   **album** - Tên album
-   **released_year** - Năm phát hành album
-   **length_min_sec** - Độ dài album (giờ, phút, giây)
-   **genre** - Thể loại album
-   **music_recording_sales_millions** - Doanh thu đĩa nhạc (triệu USD) trên [SONG://DATABASE](http://www.song-database.com?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
-   **claimed_sales_millions** - Doanh số đã tuyên bố của album (triệu USD) trên [SONG://DATABASE](http://www.song-database.com?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
-   **date_released** - Ngày phát hành album
-   **soundtrack** - Cho biết album có phải là movie soundtrack (Y - Có) hay không (N - không)
-   **rating_of_friends** - Cho biết xếp hạng từ bạn bè từ 1 tới 10
    <br>
    <br>

Có thể xem tập dữ liệu bên dưới:

<font size="1">
<table font-size:xx-small>
  <tr>
    <th>Artist</th>
    <th>Album</th> 
    <th>Released</th>
    <th>Length</th>
    <th>Genre</th> 
    <th>Music recording sales (millions)</th>
    <th>Claimed sales (millions)</th>
    <th>Released</th>
    <th>Soundtrack</th>
    <th>Rating (friends)</th>
  </tr>
  <tr>
    <td>Michael Jackson</td>
    <td>Thriller</td> 
    <td>1982</td>
    <td>00:42:19</td>
    <td>Pop, rock, R&B</td>
    <td>46</td>
    <td>65</td>
    <td>30-Nov-82</td>
    <td></td>
    <td>10.0</td>
  </tr>
  <tr>
    <td>AC/DC</td>
    <td>Back in Black</td> 
    <td>1980</td>
    <td>00:42:11</td>
    <td>Hard rock</td>
    <td>26.1</td>
    <td>50</td>
    <td>25-Jul-80</td>
    <td></td>
    <td>8.5</td>
  </tr>
    <tr>
    <td>Pink Floyd</td>
    <td>The Dark Side of the Moon</td> 
    <td>1973</td>
    <td>00:42:49</td>
    <td>Progressive rock</td>
    <td>24.2</td>
    <td>45</td>
    <td>01-Mar-73</td>
    <td></td>
    <td>9.5</td>
  </tr>
    <tr>
    <td>Whitney Houston</td>
    <td>The Bodyguard</td> 
    <td>1992</td>
    <td>00:57:44</td>
    <td>Soundtrack/R&B, soul, pop</td>
    <td>26.1</td>
    <td>50</td>
    <td>25-Jul-80</td>
    <td>Y</td>
    <td>7.0</td>
  </tr>
    <tr>
    <td>Meat Loaf</td>
    <td>Bat Out of Hell</td> 
    <td>1977</td>
    <td>00:46:33</td>
    <td>Hard rock, progressive rock</td>
    <td>20.6</td>
    <td>43</td>
    <td>21-Oct-77</td>
    <td></td>
    <td>7.0</td>
  </tr>
    <tr>
    <td>Eagles</td>
    <td>Their Greatest Hits (1971-1975)</td> 
    <td>1976</td>
    <td>00:43:08</td>
    <td>Rock, soft rock, folk rock</td>
    <td>32.2</td>
    <td>42</td>
    <td>17-Feb-76</td>
    <td></td>
    <td>9.5</td>
  </tr>
    <tr>
    <td>Bee Gees</td>
    <td>Saturday Night Fever</td> 
    <td>1977</td>
    <td>1:15:54</td>
    <td>Disco</td>
    <td>20.6</td>
    <td>40</td>
    <td>15-Nov-77</td>
    <td>Y</td>
    <td>9.0</td>
  </tr>
    <tr>
    <td>Fleetwood Mac</td>
    <td>Rumours</td> 
    <td>1977</td>
    <td>00:40:01</td>
    <td>Soft rock</td>
    <td>27.9</td>
    <td>40</td>
    <td>04-Feb-77</td>
    <td></td>
    <td>9.5</td>
  </tr>
</table></font>

<hr>

<h2 id="list">List</h2>

<h3 id="index">Chỉ mục</h3>

Chúng ta sẽ xem xét list trong Python. List là một tập hợp các đối tượng khác nhau được sắp xếp theo thứ tự như số nguyên, string và các danh sách khác. Địa chỉ của mỗi phần tử trong danh sách được gọi là <b> chỉ mục</b>. Một chỉ mục được sử dụng để truy cập và tham chiếu đến các mục trong list.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsIndex.png" width="1000" />

Hãy thử nào! Để tạo list, hãy nhập list trong dấu ngoặc vuông <b> [ ]</b>, với nội dung đặt trong dấu ngoặc đơn và được phân tách bằng dấu phẩy. Hãy thử!
"""

# Create a list

L = ["Michael Jackson", 10.1, 1982]
L

"""Chúng ta có thể sử dụng chỉ mục âm và thường với list:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsNeg.png" width="1000" />
"""

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

"""<h3 id="content">Nội dung List</h3>

List có thể chứa string, float và số nguyên. Chúng ta có thể lồng các list khác, cũng có thể lồng các tuple và các cấu trúc dữ liệu khác. Các quy ước chỉ mục tương tự áp dụng cho lồng ghép:
"""

# Sample List

["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

"""<h3 id="op">Thao tác với List</h3>

Chúng ta cũng có thể thực hiện slicing trong list. Ví dụ, nếu muốn 2 phần tử cuối cùng, có thể sử dụng lệnh sau:
"""

# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
L

"""<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsSlice.png" width="1000">

"""

# List slicing

L[3:5]

"""Chúng ta có thể sử dụng phương thức <code> extension</code> để thêm các phần tử mới vào list:

"""

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

"""Một phương thức tương tự khác là <code> append</code>. Nếu áp dụng <code> append</code> thay vì <code> extension</code>, chúng ta sẽ thêm một phần tử vào list:

"""

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

"""Mỗi khi áp dụng một phương thức, list sẽ thay đổi. Nếu áp dụng <code> extension</code>, chúng ta sẽ thêm hai phần tử mới vào list. List <code> L</code> sau đó được sửa đổi bằng cách thêm hai phần tử mới:

"""

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

"""Nếu nối list <code> ['a','b']</code>, chúng ta có một phần tử mới gồm một list lồng nhau:

"""

# Use append to add elements to list

L.append(['a','b'])
L

"""Vì list có thể thay đổi nên chúng ta có thể thay đổi chúng. Ví dụ, chúng ta có thể thay đổi phần tử đầu tiên như sau:

"""

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

"""Chúng ta cũng có thể xóa một phần tử của list bằng lệnh <code> del</code>:



"""

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

"""Chúng ta có thể chuyển đổi một string thành list bằng cách sử dụng <code> split</code>. Ví dụ: phương thức <code> split </code> dịch mọi nhóm ký tự được phân tách bằng dấu cách thành một phần tử trong list:

"""

# Split the string, default is by space

'hard rock'.split()

"""Chúng ta có thể sử dụng hàm split để tách các chuỗi trên một ký tự cụ thể. Chuyển ký tự mà chúng ta muốn tách vào đối số, trong trường hợp này là dấu phẩy. Kết quả được một list và mỗi phần tử tương ứng với một tập hợp các ký tự được phân tách bằng dấu phẩy:

"""

# Split the string by comma

'A,B,C,D'.split(',')

"""<h3 id="co">Sao chép và tạo bản sao danh sách</h3>

Khi chúng ta đặt một biến <b> B</b> bằng <b> A</b>; cả <b> A </b> và <b> B </b> đều tham chiếu đến cùng một danh sách trong bộ nhớ:
"""

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

"""<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsRef.png" width="1000" align="center">

Ban đầu, giá trị của phần tử đầu tiên trong <b> B </b> được đặt là hard rock. Nếu thay đổi phần tử đầu tiên trong <b> A </b> thành <b> banana </b>, chúng ta sẽ nhận được một tác dụng phụ không mong muốn. Vì <b> A </b> và <b> B </b> đang tham chiếu đến cùng một list, nếu chúng ta thay đổi list <b> A </b>, thì list <b> B </b> cũng thay đổi. Nếu kiểm tra phần tử đầu tiên của <b> B </b>, chúng ta được banana thay vì hard rock:
"""

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

"""Điều này được thể hiện trong hình sau:

<img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsRefGif.gif" width="1000" />

Bạn có thể tạo bản sao của list **A** bằng cách sử dụng cú pháp sau:
"""

# Clone (clone by value) the list A

B = A[:]
B

"""Biến **B** tham chiếu đến một bản sao mới hoặc bản sao của danh sách gốc; điều này được thể hiện trong hình sau:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsVal.gif" width="1000" />

Bây giờ nếu bạn thay đổi <b> A </b>, <b> B </b> sẽ không thay đổi:
"""

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

"""<h2 id="quiz">Quiz về List</h2>

Tạo danh sách <code> a_list</code>, với các phần tử <code> 1</code>, <code> hello</code>, <code> [1,2,3]</code> và <code>True</code>.
"""

# Write your code below and press Shift+Enter to execute
a_list = [1,'hello',[1,2,3],'True']
a_list

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
a_list = [1, 'hello', [1, 2, 3] , True]
a_list

```

</details>

Tìm giá trị được lưu trữ tại chỉ mục 1 của <code> a_list</code>.
"""

# Write your code below and press Shift+Enter to execute
a_list[1]

"""# <details><summary>Bấm vào đây để xem đáp án</summary>

```python
a_list[1]văn bản in đậm

```

</details>

Truy xuất các phần tử được lưu trữ tại chỉ mục 1, 2 và 3 của <code> a_list</code>.
"""

# Write your code below and press Shift+Enter to execute
a_list[1:4]

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
a_list[1:4]

```

</details>

Nối các danh sách <code> A = [1, 'a']</code> và <code> B = [2, 1, 'd']</code>:
"""

# Write your code below and press Shift+Enter to execute
A = [1 , 'a']
B = [2,1,'d']
A + B

"""<details><summary>Bấm vào đây để xem đáp án</summary>

```python
A = [1, 'a'] 
B = [2, 1, 'd']
A + B

```

</details>

<hr>
<p>Nguồn: IBM
<hr>
"""