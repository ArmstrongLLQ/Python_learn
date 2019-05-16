# -*- coding: utf-8 -*-
# MYSQL config
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'db_python3_spider'
MYSQL_TABLE = 'cookies_pool'


# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator',
	'github': 'GithubCookiesGenerator'
}
# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester',
	'github': 'GithubValidTester'
}

TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/',
	'github': 'https://github.com'
}

# API地址和端口
API_HOST = '127.0.0.1'
API_PORT = 5000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True

# 产生器和验证器循环周期
CYCLE = 240