import functools

import time

def print_run_time(func):

    @functools.wraps(func)
    def wrapper(*args,**kw):

        local_time=time.time()

        func(*args,**kw)

        t=time.time()-local_time

        print(t)

    return wrapper


@print_run_time
def test(x):

    for i in range(1000):

        print(x,end='')

        print('\n')

        return x


test(999)