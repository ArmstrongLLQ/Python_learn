from django.shortcuts import render
import logging
from django.conf import settings

logger = logging.getLogger('blog.views')
# Create your views here.

def global_setting(request):
	'''这个方法可以完成在模版里面直接调用setting.py文件里面的值，从而可以实现一些全局变量的设置
	注意：需要在setting中配置一些全局变量，并且在setting文件TEMPLATES里面的context_processors
	里面将这个方法添加进去'''
	return {
		'SITE_NAME': settings.SITE_NAME,
		'SITE_DESC': settings.SITE_DESC
	}

def index(request):
	try:
		file = open('b.txt', 'r')
	except Exception as e:
		logger.error(e)
	return render(request, 'index.html', locals())