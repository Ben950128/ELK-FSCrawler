import os
from os import path
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="Asia/taipei")

def my_job():
    if path.exists('./.fscrawler/upload_files/_status.json') is True:
        os.system('echo password | sudo -S rm -f ./.fscrawler/upload_files/_status.json')
        print('_status.json已刪除')
    else:
        print('_status.json不存在')

my_job()
sched.add_job(my_job, 'interval', minutes=1)
sched.start()