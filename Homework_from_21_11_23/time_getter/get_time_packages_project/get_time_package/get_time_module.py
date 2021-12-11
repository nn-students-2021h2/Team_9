import requests

def get_time():
    url = 'https://worldtimeapi.org/api/timezone/Europe/Moscow'
    resp = requests.get(url)
    unixtime = resp.json()['unixtime']
    return unixtime

def print_time(unixtime):
    print(unixtime)

def main():
    unixtime = get_time()
    print_time(unixtime)

if __name__ == '__main__':
    main()
