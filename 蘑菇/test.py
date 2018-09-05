# coding=utf-8
from database import DataHelper
from hashlib import sha1

# 接收用户收入
sname = input("请输入用户名：")
pwd = input("请输入密码:")

# 对密码加密
s1 = sha1()
pwd1 = pwd.encode(encoding='utf-8')
s1.update(pwd1)
pwd2 = s1.hexdigest()
# print(pwd2)


# 根据用户名查询密码
sql = 'select password from users where name = %s'
helper = DataHelper(host='10.21.103.4', user='root', database='python3',
                    port=3306, password='930902', charset='utf8')
paras = [sname]
result = helper.search(sql, paras)

# 验证
if len(result) == 0:
    print('用户名错误')
elif result[0][0] == pwd2:
    print('登陆成功')
else:
    print('密码错误')
