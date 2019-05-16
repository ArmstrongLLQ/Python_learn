# -*- coding: utf-8 -*-
import requests
import pymysql
from bs4 import BeautifulSoup

def connect_mysql(host='localhost', port=3306, user='root', passwd='root', db='db_pyton3_spider'):
	db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = db.cursor()
	return db, cursor

def get_one_page(url):
	headers = {
		"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		return response.text
	return None

def parse_one_page(html):
	soup = BeautifulSoup(html, 'lxml')
	data_list = []
	movie_list = soup.select('div.board-item-main')

	for m in movie_list:
		data_dict = {}
		data_dict['title'] = m.select('p.name')[0].get_text()
		data_dict['star'] = m.select('p.star')[0].get_text().strip()
		data_dict['release_time'] = m.select('p.releasetime')[0].get_text()
		score_int = m.select('i.integer')[0].get_text()
		score_fra = m.select('i.fraction')[0].get_text()
		data_dict['score'] = score_int + score_fra
		data_list.append(data_dict)

	return data_list

def save_data_mysql(db, cursor, data_list):
	table = 'maoyan'
	for data in data_list:
		keys = ','.join(data.keys())
		values = ','.join(['%s'] * len(data))
		sql = 'insert into {table} ({keys}) values ({values})'.format(table=table, keys=keys, values=values)
		print(sql, tuple(data.values()))
		try:
			cursor.execute(sql, tuple(data.values()))
			db.commit()
		except Exception as e:
			print(e)
			db.rollback()

def main():
	db, cursor = connect_mysql()
	for i in range(10):
		offset = i * 10

		url = 'https://maoyan.com/board/4?offset=' + str(offset)
		html = get_one_page(url)
		data_list = parse_one_page(html)
		# print(data_list)
		save_data_mysql(db, cursor, data_list)

	cursor.close()
	db.close()

if __name__ == '__main__':
	main()