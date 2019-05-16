MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

import redis
from random import choice

class RedisClient(object):
	def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
		self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

	def add(self, proxy, score=INITIAL_SCORE):
		if not self.db.zscore(REDIS_KEY, proxy):
			return self.db.zadd(REDIS_KEY, score, proxy)

	def random(self):
		result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
		if len(result):
			return choice(result)
		else:
			result = self.db.zrevrange(REDIS_KEY, 0, 100)
			if len(result):
				return choice(result)
			else:
				raise Exception

	def derease(self, proxy):
		score = self.db.zscore(REDIS_KEY, proxy)
		if score and score > MIN_SCORE:
			print('proxy:', proxy, 'now score:', score, '-1')
			return self.db.zincrby(REDIS_KEY, proxy, -1)
		else:
			print('proxy:', proxy, 'now score:', score, 'remove')
			return self.db.zrem(REDIS_KEY, proxy)

	def exists(self, proxy):
		return not self.db.zscore(REDIS_KEY, proxy) == None

	def max(self, proxy):
		print('proxy:', proxy, 'is useful, set score=', MAX_SCORE)
		return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

	def count(self):
		return self.db.zcard(REDIS_KEY)

	def all(self):
		return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

def main():
	pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
	r = redis.Redis(connection_pool=pool)

	r.zadd("zset1", {'m1': 24, 'm3':333})
	print(r.zcard("zset1"))
	print(r.zrevrange("zset1", 0, -1))
	print(r.zrevrange("zset1", 0, -1, withscores=True))
	print(r.zrangebyscore("zset1", 15, 25))
	r.zincrby("zset1", -1, "m1")
	print(r.zrevrange("zset1", 0, -1, withscores=True))

if __name__ == '__main__':
	main()