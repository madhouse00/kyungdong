#!C:\Users\Oldman\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type: text/html; charset=UTF-8\n")    #  HTML is following
print()                             # blank line, end of headers
import sys
import codecs
import cgi
import cgitb #윈도우는 cgitb 하나 더 깔아줘야 함
sys.stdout = codecs.getwriter("UTF-8")(sys.stdout.detach())
cgitb.enable() #for debegygging
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
    <li><a href="index.py?id=엄기림" target="_blank" title="엄기림">엄기림</a></li>
    <li><a href="index.py?id=주성현" target="_blank" title="주성현">주성현</a></li>
    <li><a href="index.py?id=장동진" target="_blank" title="장동진">장동진</a></li>
    <li><a href="index.py?id=김영오" target="_blank" title="김영오">김영오</a></li>
    <li><a href="index.py?id=전상준" target="_blank" title="전상준">전상준</a></li>
    <li><a href="index.py?id=최동순" target="_blank" title="최동순">최동순</a></li>
    <li><a href="index.py?id=우승재" target="_blank" title="우승재">우승재</a></li>
    <li><a href="index.py?id=박천영" target="_blank" title="박천영">박천영</a></li>
    <li><a href="index.py?id=정영상" target="_blank" title="정영상">정영상</a></li>
  </ol>
  <h3>{title}</h3>
    <p><iframe width="560" height="315" src="https://www.youtube.com/embed/kxqn8FAVbpU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>
  <p>{desc}</p>
  <img src="졸업식단체사진.jpg" width="100%"><br>
  <img src="송년회단체사진.jpg" width="100%"><br>

    
</body>
</html>
'''.format(title=pageId, desc = description))
