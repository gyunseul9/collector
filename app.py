from flask import Flask, render_template, request
import sys
import re
import datetime
from config import Configuration
from db import DBConnection,Query

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('/test/1.html')

@app.route('/sub')
##def news():
def sub():

    try:
        configuration = Configuration.get_configuration('aws')
        _host = configuration['host']
        _user = configuration['user']
        _password = configuration['password']
        _database = configuration['database']
        _port = configuration['port']
        _charset = configuration['charset']

        conn = DBConnection(host=_host,
                user=_user,
                password=_password,
                database=_database,
                port=_port,
                charset=_charset)

        kind = request.args.get('kind', default = 1, type = int)

        print('app.py:',kind)

        data = conn.exec_select(kind)

        if kind == 1:
            template = render_template('news.html',data=data)
        elif kind == 2:
            template = render_template('fishing.html',data=data)
        elif kind == 3:
            template = render_template('books.html',data=data)
        elif kind == 4:
            template = render_template('movie.html',data=data)
        elif kind == 5:
            template = render_template('jobs.html',data=data)

    except Exception as e:
        with open('/home/ubuntu/Bitbucket/collector/error.log', 'a') as file:
            file.write('{} YOU GOT AN ERROR: {}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(e)))

    return template
    ##return render_template('index.html', data=data)

##app.add_url_rule('/news','news', news)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
