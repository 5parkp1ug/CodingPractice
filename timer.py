from time import time
  
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

import math
@timer_func
def using_math(n):
    math.pow(1000000000000/2, 2)

@timer_func
def without_math(n):
    print(1000000000000*1000000000000/4)
  
  
using_math(10000000)
without_math(10000000)