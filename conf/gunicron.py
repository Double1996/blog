import multiprocessing


threads = 2
timeout = 300
bind = '127.0.0.1:8081'

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
workers_class = 'gunicorn.workers.ggevent.GeventWorker'

# 配置错误日志
logfile = '/var/log/gunicorn/debug.log'
loglevel = 'debug'
