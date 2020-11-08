from datetime import datetime
import json
from redis import Redis
from celery import Celery
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from twisted.internet import reactor

from rand_script import generate_rand_list
from blog_spider import BlogSpider, spider_results

# Uses database 1 in your local redis database
redis = Redis(db=1)

red = Redis()

#runner = CrawlerRunner()

app = Celery()
app.config_from_object('celeryconfig')


@app.task(name='task_01')
def task_01():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    if redis.exists("task_01"):
        _dict = redis.hgetall('task_01')
        # helps for auto increment during each run
        num = str(len(_dict) + 1)
        redis.hset("task_01", num, str_dt)
    else:
        redis.hset("task_01", "1", str_dt)

    task_02.delay()
    return str_dt


@app.task(name='task_02')
def task_02():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    result = spider_results()
    str_result = json.dumps(result)
    if redis.exists("task_02"):
        _dict = redis.hgetall('task_02')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        new_dict = {num: str_dt, 'result': str_result}
        redis.hmset('task_02', new_dict)
    else:
        new_dict = {'1': str_dt, 'result': str_result}
        redis.hmset('task_02', new_dict)

    task_03.delay()
    return result


@app.task(name='task_03')
def task_03():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    rand_list = json.dumps(generate_rand_list())
    if redis.exists('task_03'):
        _dict = redis.hgetall('task_03')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        new_dict = {num: str_dt, 'result': rand_list}
        redis.hmset('task_03', new_dict)
    else:
        new_dict = {'1': str_dt, 'result': rand_list}
        redis.hmset('task_03', new_dict)

    task_04.delay()
    return str_dt


@app.task(name='task_04')
def task_04():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    if redis.exists("task_04"):
        _dict = redis.hgetall('task_04')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        redis.hset("task_04", num, str_dt)
    else:
        redis.hset("task_04", "1", str_dt)
    print('done')
    return str_dt
