import requests

def get_time():
    resp = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    unixtime = resp.json()["unixtime"]
    return unixtime

def main():
    unixtime = get_time()
    print(unixtime)

if __name__ == '__main__':
    main()
