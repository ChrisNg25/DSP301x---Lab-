import re 

x = 'From: Using the : character'
y = re.findall(r'^F.+?:', x)
print(y) #['From:']

