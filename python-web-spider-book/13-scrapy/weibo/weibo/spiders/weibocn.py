# -*- coding: utf-8 -*-
import scrapy
import json
from weibo.items import WeiboItem


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/']
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&luicode=10000011&lfid=100103type=1&q={lfid}&type=uid&value={uid}&containerid=107603{uid}&page={page}'

    start_user_infos = [{
        'uid': '2687827715',
        'lfid': '欧阳娜娜'
    }, {
        'uid': '1259110474',
        'lfid': '赵丽颖'
    }]

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            for user_info in self.start_user_infos:
                yield scrapy.Request(
                    self.weibo_url.format(
                        uid=user_info.get('uid'),
                        lfid=user_info.get('lfid'),
                        page=page),
                    callback=self.parse,
                    meta={'user_info': user_info})

    def parse(self, response):
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos = result.get('data').get('cards')
            for weibo in weibos:
                myblog = weibo.get('mblog')
                if myblog:
                    item = WeiboItem()
                    field_map = {
                        'id': 'id',
                        'attitudes_count': 'attitudes_count',
                        'comments_count': 'comments_count',
                        'reposts_count': 'reposts_count',
                        'picture': 'original_pic',
                        # 'pictures': 'pics',
                        'created_at': 'created_at',
                        'source': 'source',
                        'text': 'text',
                        # 'raw_text': 'raw_text',
                        'thumbnail': 'thumbnail_pic',
                    }
                    for field, attr in field_map.items():
                        item[field] = myblog.get(attr)
                    item['user'] = response.meta.get('user_info').get('lfid')
                    yield item
