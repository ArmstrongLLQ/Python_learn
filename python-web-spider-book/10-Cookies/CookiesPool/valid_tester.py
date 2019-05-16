import json
import requests
from config import *
from db import MysqlClient
from lxml import etree


class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.mysql_client = MysqlClient(website)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        account_list = self.mysql_client.get_all()
        for account in account_list:
            self.test(account['username'], account['cookies'])


class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('正在测试Cookies', '用户名', username, 'cookies', cookies)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.mysql_client.delete_account(username)
            print('删除Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(
                test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Cookies有效', username)
            else:
                print(response.status_code, response.headers)
                print('Cookies失效', username)
                self.mysql_client.set_valid_false(username)
                print('删除Cookies', username)
        except ConnectionError as e:
            print('发生异常', e.args)


class GithubValidTester(ValidTester):
    def __init__(self, website='github'):
        ValidTester.__init__(self, website)

    def repositories(self, html):
        selector = etree.HTML(html)
        repositories = selector.xpath(
            '//*[@id="dashboard"]/div[1]/div/div[2]/ul/li/div/a/@href')
        return repositories

    def test(self, username, cookies):
        print('正在测试Cookies', '用户名', username, 'cookies', cookies)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.mysql_client.delete_account(username)
            print('删除Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(
                test_url, cookies=cookies, timeout=30, allow_redirects=False)
            if response.status_code == 200:
                if self.repositories(response.text):
                    print('Cookies有效', username)
                else:
                    print(response.status_code, response.headers)
                    print('Cookies失效', username)
                    self.mysql_client.set_valid_false(username)
                    print('删除Cookies', username)
        except ConnectionError as e:
            print('发生异常', e.args)


if __name__ == '__main__':
    WeiboValidTester().run()
