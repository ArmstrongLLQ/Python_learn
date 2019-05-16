# -*- coding: utf-8 -*-
import pymysql
from config import *
import random

class MysqlClient(object):
	def __init__(self, website):
		self.db = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USERNAME,
								  passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset='utf8',
								  cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.db.cursor()
		self.website = website

	def get_cookies_by_username(self, username):
		'''
		根据username获取cookies
		:param username:
		:return: username和cookies组成的字典
		'''
		sql = 'select * from {table} where username="{username}" and website="{website}"'.format(table=MYSQL_TABLE,
																								   website=self.website,
																								   username=username)
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()
			print(result)
			return result
		except Exception as e:
			print(e)

	def update_cookies_by_username(self, username, cookies):
		'''
		根据username更新cookies
		:param username:
		:param cookies:
		:return:
		'''
		sql = 'update {table} set cookies=\'{cookies}\', valid=1 where username="{username}" and website="{website}"'.format(				table=MYSQL_TABLE, cookies=cookies, username=username, website=self.website)
		print(sql)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as e:
			print(e)
			self.db.rollback()

	def get_all(self):
		'''
		获取所有的数据 username，password，cookies
		:return:数据的字典列表
		'''
		sql = 'select * from {table} where website="{website}"'.format(table=MYSQL_TABLE, website=self.website)
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()
			# print(result)
			return result
		except Exception as e:
			print(e)

	def get_cookies_random(self):
		data_list = self.get_all()
		data = random.choice(data_list)
		cookies = data['cookies']
		print(cookies)
		return cookies

	def delete_account(self, username):
		'''
		删除无效的账号密码
		:param username:
		:return:
		'''
		sql = 'delete from {table} where username="{username}"'.format(table=MYSQL_TABLE, username=username)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as e:
			print(e)
			self.db.rollback()

	def set_valid_false(self, username):
		'''
		将无效的cookies设置为0
		:param username:
		:return:
		'''
		sql = 'update {table} set valid=0 where username="{username}" and website="{website}"'.format(				table=MYSQL_TABLE, username=username, website=self.website)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as e:
			print(e)
			self.db.rollback()

	def test(self):
		sql = 'select * from ' + MYSQL_TABLE
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchone()
			print(result)
		except Exception as e:
			print(e)

if __name__ == '__main__':
	mysql_client = MysqlClient('zhihu')
	# mysql_client.get_all()
	# mysql_client.get_cookies_by_username('test1')
	# mysql_client.update_cookies_by_username('test1', 'test_cookies')
	mysql_client.get_cookies_random()



