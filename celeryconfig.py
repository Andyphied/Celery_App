from celery.schedules import crontab

result_backend = "redis://"
broker_url = 'redis://localhost:6379/0'

task_serilizer = 'json'

result_serilizer = 'json'

# The beat schedule settings
beat_schedule = {
    'start scrape': {
        'task': 'task_01',
        'schedule': crontab(minute='*/2')
    },
}