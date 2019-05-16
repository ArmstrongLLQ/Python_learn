import requests

headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "keep-alive",
		'Host': '121.42.164.187:8088',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36',
		# 'Cookie': 'csrftoken=JoLrxnCqKWxVAjwpNZ6IxyQYc3ZSIh1FNP3IP7LLj3GHjswM6xKaCXfg1OXkQVQp; sessionid=44d6kbtll1ckyr15ugtcwf5ph9ipxcvl'
		}
cookies = {'Cookie':'csrftoken=JoLrxnCqKWxVAjwpNZ6IxyQYc3ZSIh1FNP3IP7LLj3GHjswM6xKaCXfg1OXkQVQp; sessionid=44d6kbtll1ckyr15ugtcwf5ph9ipxcvl'}


response = requests.get('http://121.42.164.187:8088/zhiku_api/details/?format=json', cookies=cookies)
print(response.json())