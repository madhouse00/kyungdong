#!C:\Users\Oldman\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type: text/html; charset=UTF-8\n")    #웹서버가 응답하면서 내가 너한테 보내줄 컨텐츠는 text고 html이야
print()                             # blank line, end of headers
import sys
import codecs
import cgi, cgitb, os
import cgitb #윈도우는 cgitb 하나 더 깔아줘야 함
sys.stdout = codecs.getwriter("UTF-8")(sys.stdout.detach()) #한글 문제
cgitb.enable() #for debegygging

#id값으로 목록 만들기
files = os.listdir('data')      #files는 data 디렉토리값을 가져온 리스트이다
listStr = ''
for item in files: #files에 있는 것들을 item에 변수로 담는다
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item) #기존 값에 item에 있는거 더함
#기존 비어있는 listStr에 엄기림이 더해지고 엄기림에 그 다음 항목이 더해지고 이게 반복

#id값이 존재하냐 안하냐에 따라서
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    #pageId = form.getvalue('id')   도 가능
    description = open('data/'+pageId, 'r', encoding = 'UTF-8').read() #읽기 형식으로 data 디렉토리의 pageId에 해당되는 것들을 가져와서 description에 씌운다
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId) #format에 의해서 {}부분이 ()안의 값으로 대체된다.
    #update링크가 id값이 없다면 업데이트할 대상이 없다
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)

else:
    pageId = '안녕하지비!'
    description = '우리들의 일그러진 단체사진입니다.'
    update_link = ''
    delete_action = ''




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
    {update_link}
    {delete_action}
    <h3>{title}</h3>
    <p>{desc}</p>
    <img src="졸업식단체사진.jpg" width="100%"><br>
    <img src="송년회단체사진.jpg" width="100%"><br>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))
