
import re

p = re.compile("a[.]{3,}b")

print(p.math("accb"))
print(p.math("a....b"))
print(p.math("aaab"))
print(p.match("a.ccb"))












import re
p = re.compile("[a-z]+")
m = p.__search("5 python")
print(m.start())
print(m.end()) 
print(m.start() + m.end())











import re
s = """
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####",s)

print(result)












pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.math("pahkey@gmail.com"))
print(pat.math("kim@gdaum.net"))
print(pat.math("pahkey@myhome.co.kr"))
