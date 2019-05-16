# -*- coding: utf-8 -*-
'''
模拟登陆github
'''
import requests
from lxml import etree

class Login(object):
	def __init__(self):
		self.headers = {
			'Referer': 'https://github.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36',
			'Host': 'github.com'
		}
		self.login_url = 'https://github.com/login'
		self.post_url = 'https://github.com/session'
		# 个人详情页面
		self.logined_url = 'https://github.com'
		# 创建一个session，维持一个会话，可以自动处理cookies
		self.session = requests.Session()

	def token(self):
		response = self.session.get(self.login_url, headers=self.headers)
		selector = etree.HTML(response.text)
		token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
		print(token)
		return token

	def login(self, username, password):
		post_data = {
			'commit': 'Sign in',
			'utf8': '✓',
			'authenticity_token': self.token(),
			'login': username,
			'password': password
		}
		response = self.session.post(self.post_url, data=post_data, headers=self.headers)
		# 由于requests自动处理了重定向信息，登录成功之后可以直接跳转到首页，首页会显示所关注人的动态信息，得到响应后
		# 使用dynamics方法对其进行处理
		if response.status_code == 200:
			print('login success')
			# print(response.text)
			self.repositories(response.text)

		# 接下来在用Session对象请求个人详情页，然后用prifile方法处理个人详情页信息
		# 这里了Session，一直在同一个对话下get所有的页面，所以会自动处理cookies
		response= self.session.get(self.logined_url, headers=self.headers)
		if response.status_code == 200:
			self.repositories(response.text)
			print(response.cookies)

	def repositories(self, html):
		selector = etree.HTML(html)
		repositories = selector.xpath('//*[@id="dashboard"]/div[1]/div/div[2]/ul/li/div/a/@href')
		print(repositories)


if __name__ == '__main__':
	login = Login()
	login.login(username='ArmstrongLLQ', password='lilanqing921207')