import requests
from get_custom_logger import get_logger
import time

def flask_echo_test():
    logger = get_logger('Echo_test')
    g_data= {'text': 'echo'}
    n = 50
    t_diff = 0
    while t_diff < 1:
        t_start = time.time()
        for i in range(n):
            r = requests.get('http://127.0.0.1:5000/echo', params=g_data)
        t_end = time.time()
        t_diff = t_end - t_start
        n += 5
    logger.info(f"Flask_server approximately {n} in one second({t_diff})")

def flask_cpu_bound_test():
    logger = get_logger('Cpu_bound_test')
    g_data= {'n': '25'}
    t_start = time.time()
    r = requests.get('http://127.0.0.1:5000/cpu_bound', params=g_data)
    print(r.text)
    t_end = time.time()
    t_diff = t_end - t_start
    logger.info(f"Flask_server fibonacci of {g_data['n']} calculate for {t_diff}")

if __name__=="__main__":
    flask_cpu_bound_test()


