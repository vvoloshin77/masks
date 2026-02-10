import traceback

def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f'{func.__name__} ok\n'
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
            except Exception as e:
                error_type = traceback.format_exc().strip().split('\n')[-1]
                log_message = f'{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}\n'
                result = None
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
            return result
        return wrapper
    return decorator


@log(filename=None)
def my_function(x, y):
    return x + y

print(my_function('',2))


