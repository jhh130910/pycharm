import threading
lock = threading.Lock()
item = 1
my_list = []

lock.acquire()
try:
    my_list.append(item)
finally:
    lock.release()

#
with lock:
    my_list.append(item)
