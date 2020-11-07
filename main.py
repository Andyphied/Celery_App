from datetime import datetime
from redis import Redis
from celery import Celery

# Uses database 1 in your local redis database
redis = Redis(db=1)

app = Celery()
app.config_from_object('celeryconfig')


@app.task(name='task_01')
def task_01():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    if redis.exists("task_01"):
        _dict = redis.hgetall('task_01')
        #helps for auto increment during each run
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
    if redis.exists('task_01'):
        _dict = redis.hgetall('task_01')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        redis.hset("task_02", num, str_dt)
    else:
        redis.hset("task_02", "1", str_dt)

    task_03.delay()
    return str_dt


@app.task(name='task_03')
def task_03():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    if redis.exists("task_01"):
        _dict = redis.hgetall('task_01')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        redis.hset("task_03", num, str_dt)
    else:
        redis.hset("task_03", "1", str_dt)

    task_04.delay()
    return str_dt


@app.task(name='task_04')
def task_04():
    date_time = datetime.now()
    str_dt = str(date_time.isoformat)
    if redis.exists("task_01"):
        _dict = redis.hgetall('task_01')
        #helps for auto increment during each run
        num = str(len(_dict) + 1)
        redis.hset("task_04", num, str_dt)
    else:
        redis.hset("task_04", "1", str_dt)
    print('done')
    return str_dt
