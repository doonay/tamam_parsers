import time
import ps_parser
import async_ps_parser
import async_ps_parser_optimized

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time} секунд.")
        return result
    return wrapper

@timer_decorator
def speed_test():
    ps_parser.ps_parser()

@timer_decorator
def speed_test():
    async_ps_parser.ps_parser()

@timer_decorator
def speed_test():
    async_ps_parser_optimized.ps_parser()

speed_test() # Вызов функции с замером времени выполнения