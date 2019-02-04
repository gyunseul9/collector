import pymysql

class DBConnection:
        def __init__(self,host,user,password,database,charset,port):
                self.connection = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        db=database,
                        charset=charset,
                        port=port,
                        cursorclass=pymysql.cursors.DictCursor)

        def exec_select(self,kind):
                with self.connection.cursor() as cursor:
                        query = Query().get_select(kind)
                        cursor.execute(query)
                        data = cursor.fetchall()

                return data

        def close(self):
                self.connection.close()

        def commit(self):
                self.connection.commit()

class Query:
        def get_select(self,kind):
            
                if kind == 1:
                    table = 'news'
                    condition = ''
                    sort = 'order by num desc limit 5'
                elif kind == 2:
                    table = 'fishing'
                    condition = ''
                    sort = 'order by num desc limit 5'
                elif kind == 3:
                    table = 'books'
                    condition = 'where ranking <= 10'
                    sort = 'order by num desc limit 10'
                elif kind == 4:
                    table = 'movie'
                    condition = 'where update_date=curdate() - interval 1 day'
                    sort = ''
                elif kind == 5:
                    table = 'jobs'
                    condition = ''
                    sort = 'order by num desc limit 5'

                print('db.py:get_select:',kind,table)

                query = 'select * from {} {} {}'.format(table,condition,sort)

                return query

