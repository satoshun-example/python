import time
from threading import Thread

def count(n):
    while n > 0:
        n -= 1

value = 10 ** 8

before = time.time()
print('do not Use thread')
count(value)
print('finish: %f seconds' % (time.time() - before))

before = time.time()
print('Use thread')
t1 = Thread(target=count, args=(value / 2,))
t2 = Thread(target=count, args=(value / 2,))
t1.start()
t2.start()
t1.join()
t2.join()
print('finish: %f seconds' % (time.time() - before))
