# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('add_tasks', broker='redis://127.0.0.1:6379/1')

@app.task
def add(x, y):
    print "klx"
    return x + y
