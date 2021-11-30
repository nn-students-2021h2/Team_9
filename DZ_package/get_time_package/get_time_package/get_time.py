import sys
import requests
try:
    from pretty_print_package import pretty_print 
except ImportError:
    pass

def get_time():
    resp = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    unixtime = resp.json()["unixtime"]
    return unixtime

def print_time(unix):
    print(unix)

def main():
    unixtime = get_time()
    if 'pretty_print_package' in sys.modules:
        pretty_print.print_time_pretty(unixtime)
    else:
        print_time(unixtime)

if __name__ == '__main__':
    main()
