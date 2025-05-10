def create_decorator(_func=None, *, commit=False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            retval = function(*args, **kwargs)
            print(commit)
            return retval

        return wrapper

    if _func is None:
        return decorator

    return decorator(_func)


@create_decorator(commit=True)
def test():
    return 1


print(test())
