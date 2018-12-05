import redis
import pymysql
 
try:
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
    print("connected success.")
except:
    print("could not connect to redis.")

r = redis.Redis(connection_pool=pool)

#list = '300033,600066'
#r.set('stock_codes', list)
 
#list = str(r.get('stock_codes'))

#print(list)

#pipe = r.pipeline()
#pipe.set('name', '张三')
#pipe.set('hello', 'world')
#pipe.execute()

#name = r.get('name').decode('utf-8')
#hello = r.get('hello')
#print(name, hello)

user = input('请输入用户名：')
pwd = input('请输入密码：')

db = pymysql.connect(host='127.0.0.1', user='shepherd', password='Sinitek@pm1', database='flask_blog', charset='utf8')
link = db.cursor()
link.execute('select * from admin where username=%s and password=%s',(user, pwd))
data = link.fetchall()

username = r.get('username')
password = r.get('password')

if(username):
    username = username.decode('utf-8')
    password = password.decode('utf-8')
    if(username==user and password==pwd):
        print('登录成功，正在使用缓存数据')
    else:
        print('登录失败,用户名或密码错误')
else:
    if(data):
        r.set('username',user)
        r.set('password',pwd)
        print('数据库验证成功')
    else:
        print('数据库验证失败')
