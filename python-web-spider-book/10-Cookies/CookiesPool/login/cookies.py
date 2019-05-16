# -*- coding: utf-8 -*-
import requests

class WeiboCookies():
	def __init__(self, username, password):
		self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https://m.weibo.cn/'
		self.headers = {
			'Referer': 'https://m.weibo.cn/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36',
			'Host': 'passport.weibo.cn'
		}
		self.logined_url = 'https://m.weibo.cn/profile/2630640297'
		self.username = username
		self.password = password

	def open(self):
		'''
		打开网页,获取cookies
		:return:
		'''
		response = requests.post(self.url, data={'LoginName':self.username, 'LoginPassword':self.password}, headers=self.headers)
		if response.status_code == 200:
			print('login success')
			cookies = response.cookies
			return {
				'status': 1,
				'content': cookies
			}
		else:
			return {
				'status': 3,
				'content': 'login failed'
			}

class GithubCookies():
	def __init__(self, username, password):
		self.headers = {
			'Referer': 'https://github.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36',
			'Host': 'github.com'
		}
		self.login_url = 'https://github.com/login'
		self.post_url = 'https://github.com/session'
		self.username = username
		self.password = password
		self.session = requests.Session()

	def token(self):
		response = self.session.get(self.login_url, headers=self.headers)
		from lxml import etree
		selector = etree.HTML(response.text)
		token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
		print(token)
		return token

	def open(self):
		'''
		打开网页,获取cookies
		:return:
		'''
		post_data = {
			'commit': 'Sign in',
			'utf8': '✓',
			'authenticity_token': self.token(),
			'login': self.username,
			'password': self.password
		}
		response = self.session.post(self.post_url, data=post_data, headers=self.headers)
		print(response.status_code)
		if response.status_code == 200:
			print('login success')
			cookies = response.cookies
			return {
				'status': 1,
				'content': cookies
			}
		else:
			return {
				'status': 3,
				'content': 'login failed'
			}

if __name__ == '__main__':
	# weibo_cookies = WeiboCookies('13261903822', 'lilanqing921207')
	# weibo_cookies.open()
	github_cookies = GithubCookies('ArmstrongLLQ', 'lilanqing921207')
	github_cookies.open()