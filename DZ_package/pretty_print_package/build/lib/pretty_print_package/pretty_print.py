from datetime import datetime
from get_time_package.get_time import get_time

def print_time_pretty(unixtime):
    formated_time = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    print(formated_time)

def main():
    unix = get_time()
    print_time_pretty(unix)

if __name__== "__main__":
    main()
