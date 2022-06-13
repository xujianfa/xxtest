from flask import Flask
from flask_apscheduler import APScheduler
import datetime
from flask_apscheduler.auth import HTTPBasicAuth
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


def pt(i, j):
    print('这是一个函数%s%s' % (i, j))


class Config(object):
    JOBS = [
        {
            'id': 'job1',  # 一个标识
            'func': pt,  # 指定运行的函
            'args': (1, 2),
            'trigger': 'interval',  # 指定 定时任务的类型
            'seconds': 2,  # 运行的间隔时间
            'replace_existing': True
        }
    ]
    # 存储定时任务（默认是存储在内存中）
    # 设置时区，时区不一致会导致定时任务的时间错误
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # 一定要开启API功能，这样才可以用api的方式去查看和修改定时任务
    SCHEDULER_API_ENABLED = True
    # api前缀（默认是/scheduler）
    SCHEDULER_API_PREFIX = '/scheduler'
    # 配置允许执行定时任务的主机名
    SCHEDULER_ALLOWED_HOSTS = ['*']
    # auth验证。默认是关闭的，
    SCHEDULER_AUTH = HTTPBasicAuth()
    # 设置定时任务的执行器（默认是最大执行数量为10的线程池）
    SCHEDULER_EXECUTORS = {'default': {'type': 'threadpool', 'max_workers': 10}}
    # 另外flask-apscheduler内有日志记录器。name为apscheduler.scheduler和apscheduler.executors.default。如果需要保存日志，则需要对此日志记录器进行配置


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app


app = create_app()


@app.route('/')
def pp():
    print('xujainfa')
    return 'xujianfa'


app.run(host='127.0.0.1', port='7788')
