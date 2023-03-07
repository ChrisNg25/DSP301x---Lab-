import re

str='The advancements in biomarine studies franky@google.com, with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
#Type your answer here.
regex = r'(\w+)@' #regex= '([\w]*)@'   # \w là lọc chuỗi và số, sau đó kết thúc bằng @, phần trong ngoặc tròn sẽ được findall
emails=re.findall(regex, str)
print('Email: ',emails)