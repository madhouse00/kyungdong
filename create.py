#!C:\Users\Oldman\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type: text/html; charset=UTF-8\n")    #  HTML is following
print()                             # blank line, end of headers
import sys
import codecs
import cgi, cgitb, os
import cgitb #윈도우는 cgitb 하나 더 깔아줘야 함
sys.stdout = codecs.getwriter("UTF-8")(sys.stdout.detach())
cgitb.enable() #for debegygging

files = os.listdir('data')      #files는 리스트이다
listStr = ''
for item in files: #files에 있는 것들을 item에 변수로 담는다
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item) #기존 값에 item에 있는거 더함
#기존 비어있는 listStr에 엄기림이 더해지고 엄기림에 그 다음 항목이 더해지고 이게 반복

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    #pageId = form.getvalue('id')   도 가능
    description = open('data/'+pageId, 'r', encoding = 'UTF-8').read()
else:
    pageId = '안녕하지비!'
    description = '우리들의 일그러진 단체사진입니다.'
print('''<!doctype html>
<html>
<head>
    <title>안녕하시라요 - html</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href=index.py title="안녕하지비">안녕하시라요!!</a></h1>
    <p>안녕하세요. 밑도끝도 없는 소개 사이트입니다.<br>
    우리 친구들을 소개합니다</p>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
    <img src="졸업식단체사진.jpg" width="100%"><br>
    <img src="송년회단체사진.jpg" width="100%"><br>
</body>
</html>
'''.format(title=pageId, desc = description, listStr = listStr))
