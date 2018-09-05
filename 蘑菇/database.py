import pymysql as pys


class DataHelper(object):
    def __init__(self, host, user, database, port, password, charset):
        self.host = host
        self.user = user
        self.database = database
        self.port = port
        self.password = password
        self.charset = charset
        self.conn = None
        self.cursor = None
        self.data = None

    def mysql_connection(self):
        self.conn = pys.connect(host=self.host, user=self.user, database=self.database,
                                port=self.port, password=self.password, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def opreration(self, sql, paras):
        try:
            self.mysql_connection()
            self.cursor.execute(sql, paras)
            self.conn.commit()
            self.data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)

    def add(self, sql, paras):
        self.opreration(sql, paras)

    def delete(self, sql, paras):
        self.opreration(sql, paras)

    def search(self, sql, paras):
        self.opreration(sql, paras)
        return self.data

    def update(self, sql, paras):
        self.opreration(sql, paras)


# my_database = DataHelper(host='10.21.103.4', user='root', database='python3',
#                          port=3306, password='930902', charset='utf8')
# my_sql = 'select * from students'
# my_sql = 'insert into students(name) values("王小二")'
# my_sql = 'update students set name="王二小" where id = 8 '
# my_sql = 'delete from students where id = 8'
# my_database.add(my_sql)


