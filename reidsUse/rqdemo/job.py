# -*- encoding:utf-8 -*-

from redis import Redis
from rq import Queue, Connection
from rqFunction import rqTest



redis_host = '120.78.198.108'
redis_port = 6379
redis_conn = Redis(host=redis_host, port=redis_port,db=1)
with Connection(redis_conn):
    q = Queue('slt_log')
    result = q.enqueue(rqTest, 'abc')