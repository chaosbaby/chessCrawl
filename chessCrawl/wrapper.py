import json
import time


def timed(func):
    """
    records approximate durations of function calls
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        print("{name:<30} started".format(name=func.__name__))
        result = func(*args, **kwargs)
        duration = "{name:<30} finished in {elapsed:.2f} seconds".format(
            name=func.__name__, elapsed=time.time() - start
        )
        print(duration)
        return result

    return wrapper


def argsCombine(args1, args2):
    args = list(args1)
    replaceArgs = list(args2)

    for i in range(len(args1)):
        if args1[i] == None:
            args[i] = replaceArgs.pop(0)
    args.extend(replaceArgs)
    return args


def kwargsCombine(kwargs1, kwargs2):
    return {**kwargs1, **kwargs2}


from functools import wraps


def preArgs(*pargs, **pkwargs):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            newkwargs = kwargsCombine(pkwargs, kwargs)
            newArgs = argsCombine(pargs, args)

            ret = func(*newArgs, **newkwargs)
            return ret

        return wrapper

    return decorate


def jsonfy(item):
    return json.dumps(item, ensure_ascii=False)


def jsonfy_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if __name__ == "__main__":
            return jsonfy(ret)
        else:
            return ret

    return wrapper


from clize import Parameter


def process_parameter(parameter_name, process_func):
    def decorator(func):
        # def wrapper(*args, **kwargs: Parameter.IGNORE):
        @wraps(func)
        def wrapper(*args, **kwargs: Parameter.IGNORE):
            if __name__ == "__main__":
                if parameter_name in kwargs:
                    kwargs[parameter_name] = process_func(kwargs[parameter_name])
                elif (
                    len(args) > 0
                    and len(func.__code__.co_varnames) > 0
                    and func.__code__.co_varnames[0] == parameter_name
                ):
                    args = list(args)
                    args[0] = process_func(args[0])
            return func(*args, **kwargs)

        return wrapper

    return decorator


class ADict(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def __delattr__(self, attr):
        del self[attr]
