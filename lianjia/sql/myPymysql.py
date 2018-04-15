import pymysql
from 项目.log.myLogging import logging_handle

logger = logging_handle('myPymysql')

class DBHelper:
    def __init__(self, host='localhost', user='root', password='123456', port=3306, db='maoyan', charset='utf8'):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.db = db
        self.conn = None
        self.cur = None
        self.charset = charset

    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password, db=self.db, charset=self.charset)
        except:
            logger.error('connectDatabase error')
            return False
        logger.info('connect success')
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据库打开，则关闭，否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
            logger.info('close mysql success')
        return True

    # 执行数据库的sql语句
    def execute(self, sql, params=None):
        if not self.connectDatabase():
            logger.error('mysql connect failed')
        try:
            if self.conn and self.cur:
                print(sql)
                self.cur.execute(sql, params)
                self.conn.commit()
                logger.info('execute success：' + sql)
        except:
            logger.error('mysql execute failed: ' + sql)
            logger.error('params: ' + params)
            return False
        return True

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchall()


if __name__ == '__main__':
    dbhelper = DBHelper()
    sql = "insert into movie values('asjhjhf', 'wet', 'yui', '2008');"
    dbhelper.connectDatabase()
    try:
        dbhelper.execute(sql)
        logger.info('insert success：' + sql)
    except:
        logger.error('insert error：' + sql)
    finally:
        dbhelper.close()
