from functools import wraps


#Gives function-based API views a lot of the same capabilities as class-based views
def define_usage(params=None, returns=None):
    def decorator(function):
        cls = function.view_class
        header = None
        # Build a list of the valid methods, but take out 'OPTIONS'
        methods = [method.upper() for method in cls.http_method_names if method != 'options']
        # Build response dictionary
        usage = {'Request Types': methods, 'Headers': header, 'Body': params, 'Returns': returns}

        # Prevent side effects
        @wraps(function)
        def _wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        _wrapper.usage = usage
        return _wrapper
    return decorator
#Этот декоратор предоставляет четыре информационных элемента: типы запросов, заголовки, параметры и возвращаемое значение каждой функции.