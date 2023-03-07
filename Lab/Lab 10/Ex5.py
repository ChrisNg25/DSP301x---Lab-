import re

str='''Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores.'''

#Type your answer here.

regex= '(\w{8,8})'   # \w thay thế cho cụm chữ hoặc số, {8,8} là giới hạn ký tự tối thiểu, tối đa của chuỗi, phần trong ngoặc sẽ được findall
match=re.findall(regex, str)
print(match)
