from __future__ import absolute_import

from celery import Celery

app = Celery('proj',
             broker='redis://',
             backend='redis://',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=6379,
)

if __name__ == '__main__':
    app.start()