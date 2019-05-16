# -*- coding: utf-8 -*-

import json

from config import *
from db import MysqlClient
from login.cookies import WeiboCookies, GithubCookies


class CookiesGenerator(object):
	def __init__(self, website='default'):
		self.website = website
		self.mysql_client = MysqlClient(website)

	def new_cookies(self, username, password):
		"""
		新生成Cookies，子类需要重写
		:param username: 用户名
		:param password: 密码
		:return:
		"""
		raise NotImplementedError

	def process_cookies(self, cookies):
		'''
		处理cookies
		:param cookies:
		:return:
		'''
		dict = {}
		for k, v in cookies.items():
			dict[k] = v

		print(dict)
		return dict

	def run(self):
		"""
		运行, 得到所有账户, 然后顺次模拟登录
		:return:
		"""
		account_list = self.mysql_client.get_all()
		# print(account_list)

		for account in account_list:
			if account['valid'] == 0:
				print('正在生成Cookies...', '账号', account['username'], '密码', account['password'])
				result = self.new_cookies(account['username'], account['password'])
				# 成功获取
				if result.get('status') == 1:
					cookies = self.process_cookies(result.get('content'))
					print('成功获取到Cookies', cookies)
					self.mysql_client.update_cookies_by_username(account['username'], json.dumps(cookies))
				#密码错误，移除账号
				elif result.get('status') == 2:
					print(result.get('content'))
					if self.mysql_client.delete_account(account['username']):
						print('成功删除账号')
				else:
					print(result.get('content'))

		print('所有账号都已经成功获取Cookies')

class WeiboCookiesGenerator(CookiesGenerator):
	def __init__(self, website='weibo'):
		"""
		初始化操作
		:param website: 站点名称
		:param browser: 使用的浏览器
		"""
		CookiesGenerator.__init__(self, website)

	def new_cookies(self, username, password):
		"""
		生成Cookies
		:param username: 用户名
		:param password: 密码
		:return: 用户名和Cookies
		"""
		return WeiboCookies(username, password).open()

class GithubCookiesGenerator(CookiesGenerator):
	def __init__(self, website='github'):
		"""
		初始化操作
		:param website: 站点名称
		:param browser: 使用的浏览器
		"""
		CookiesGenerator.__init__(self, website)

	def new_cookies(self, username, password):
		"""
		生成Cookies
		:param username: 用户名
		:param password: 密码
		:return: 用户名和Cookies
		"""
		return GithubCookies(username, password).open()

if __name__ == '__main__':
	# genetor = WeiboCookiesGenerator()
	# genetor.run()
	genetor = WeiboCookiesGenerator()
	genetor.run()