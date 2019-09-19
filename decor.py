import time, functools

def clock(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return wrapper




def decor(func):
    def wrapper():
        return func().upper()
    return wrapper

def strong(func):
    def wrapper():
        return '<strong>'+ func()+'</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<emp>' + func() + '</emp>'
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(args[0].upper(),args[1].capitalize())
        return func(*args, **kwargs)
    return wrapper

