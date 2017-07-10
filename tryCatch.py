import urllib.request as request


arr = ['http://www.baidu.com','https://stage.ybj.com/userFront/']

for item in arr:
    try:
        current = request.urlopen(item).getcode()
        current==200
        print("ok")
    except Exception as erro:
        print('this is a ' + str(erro))   
