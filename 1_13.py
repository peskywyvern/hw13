# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):
# methods:
#   - to_int
#   - to_str
#   - to_bool
#   - to_float
#
# Don't forget to use @wraps

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if arg.isdigit():
                    return int(arg)
            return 'Conversion is impossible'
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            return str(*args)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if arg.lower() == 'true':
                    return True
                if arg.lower() == 'false':
                    return False
            return 'Conversion is impossible'
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            try:
                return float(*args)
            except ValueError:
                return 'Conversion is impossible'
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
