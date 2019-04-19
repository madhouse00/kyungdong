#!C:\Users\Oldman\AppData\Local\Programs\Python\Python37-32\python.exe

import sys
import codecs
sys.stdout = codecs.getwriter("UTF-8")(sys.stdout.detach()) #한글 문제

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value #pageId를 별도로 받기 위해서
title = form["title"].value
description = form["description"].value


opened_file = codecs.open('data/'+pageId, 'w', 'utf-8') #opened_file이라는 변수가 data 디렉토리 아래 title을 붙여서 써넣는 것을 가리킴
opened_file.write(description)
#opened_file의 description에 해당되는 값이 data/ +title이라는 곳에 써지도록 한다.
opened_file.close()
#파일을 연 다음 작업이 끝난 뒤엔 파일을 닫아야 한다.
#특히 쓰기 할 때 무조건 붙여줘야 한다.

os.rename('data/'+pageId, 'data/'+title)
#data 디렉토리 안의 pageId의 이름과 title의 이름을 바꿔준다

#Redirection 사용자를 웹서버가 다른 페이지로 보내버리는 헤더를 말한다.
#컨텐츠를 사용자들이 생산하는 방법
#데이터를 어떻게 받아서 어떻게 저장하는지#
print("Location: index.py?id="+title)
#index.py?id=는 우리가 생성한 파일의 값을 주고 title 웹브라우저에게 웹서버가 이 주소로 이동해 라고 하면 앞에 Location: 붙이면 된다
print()
