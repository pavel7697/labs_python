# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
from datetime import datetime
import contextlib

@contextlib.contextmanager

def timer():
    t1=datetime.now()
    yield
    t2=datetime.now()
    result=t2-t1
    res=str(result.seconds)+'.'+str(result.microseconds)
    print (res)