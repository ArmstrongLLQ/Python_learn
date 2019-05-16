from flask import Flask, g, render_template
from config import *
from db import *

__all__ = ['app']

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='CookiesPool')


def get_conn():
    """
    获取
    :return:
    """
    for website in GENERATOR_MAP:
        print('MysqlClient(' + '"' +  website + '"' + ')')
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('MysqlClient(' + '"' +  website + '"' + ')'))
    return g


@app.route('/random/<website>')
def random(website):
    """
    获取随机的Cookie, 访问地址如 /weibo/random
    :return: 随机Cookie
    """
    g = get_conn()
    cookies = getattr(g, website + '_cookies').get_cookies_random()
    return cookies

# @app.route('/add/<website>/<username>/<password>')
# def add(website, username, password):
#     """
#     添加用户, 访问地址如 /weibo/add/user/password
#     :param website: 站点
#     :param username: 用户名
#     :param password: 密码
#     :return:
#     """
#     g = get_conn()
#     print(username, password)
#     getattr(g, website + '_cookies').set(username, password)
#     return json.dumps({'status': '1'})

if __name__ == '__main__':
    app.run(debug=True)
