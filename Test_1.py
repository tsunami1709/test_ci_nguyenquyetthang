import re

str = input("Nhập vào 1 dãy số, cách nhau bởi dấu ' ':")
x = re.sub("\s","\n", str)

print("Dãy số vừa nhập:")
print(x)
