str1 = "hello world!"
f = open('helloworld.html','w')
message = """
<html>
<head></head>
<body>
<p>Welcome</p>
<p>%s</p>
</body>
</html>"""%(str1)

f.write(message)
f.close()