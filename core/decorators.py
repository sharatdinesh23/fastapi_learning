import time 

def log_execution(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        execution_time = time.time() - start_time
        
        print(f"{func.__name__} took {execution_time:.10f} seconds")
        return result
    return wrapper
 