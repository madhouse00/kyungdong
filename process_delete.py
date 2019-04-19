#!C:\Users\Oldman\AppData\Local\Programs\Python\Python37-32\python.exe

import sys
import codecs
sys.stdout = codecs.getwriter("UTF-8")(sys.stdout.detach()) #한글 문제

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)





#Redirection
print("Location: index.py")
#삭제가 끝난 다음엔 홈페이지로 이동
print()
