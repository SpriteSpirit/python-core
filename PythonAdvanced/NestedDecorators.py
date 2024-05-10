from functools import cache, wraps  # Декоратор кеша, warps помогает декорировать др. функции

#
# @cache  # будет кешировать результат, который связан с аргументом
# def fib(n):
#     """
#     0 1 1 2 3 5 8 13
#     """
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# # fib = cache(fib)
# # кэширование - позволяет избежать лишних вычислений или обращений
# print(fib(50))
# print([fib(n) for n in range(11)])


# 2. Функция кеширования вручную
# def cached(func):
#     """
#
#     :param func: Функция, кот. будет декорирована
#     :return: Функцию из декоратора
#     """
#
#     results = {}
#
#     @wraps(func)
#     def wrapped(n):
#         if n not in results:
#             results[n] = func(n)
#         return results[n]
#
#     return wrapped
#
#
# @cached
# def fib(n):
#     """
#     0 1 1 2 3 5 8 13
#     """
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(50))
# print([fib(n) for n in range(5, 10)])

# 3. декоратор для нескольких аргументов
# показывает, какие вызовы были сделаны над этой функцией
# * - означает, что не нужно передавать далее ничего кроме именованных аргументов
def trace(_func=None, *, sep='='):

    def decorator(func):
        func.calls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            """

            :param args: любое кол-во позиционных аргументов (tuple)
            :param kwargs: любое кол-во именованных аргументов (dict)
            :return:
            """
            func.calls += 1
            print(sep * func.calls, f'-> {func.__name__}(*{args}, **{kwargs})')
            try:
                return func(*args, **kwargs)
            finally:
                print(sep * func.calls, f'-> {func.__name__}(*{args}, **{kwargs})')
                func.calls -= 1

        return wrapper

    if _func:
        return decorator(_func)
    return decorator


# @trace('~')
@trace
@cache
def fib(n):
    """
    0 1 1 2 3 5 8 13
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(3))
# print([fib(n) for n in range(5, 10)])
