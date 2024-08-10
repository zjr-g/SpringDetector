import requests
import datetime
import configparser

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
    'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00']


# 获取当前时间(格式化)
def getLastDate():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 读取目录文件
def read_dir_file(filename):
    with open(filename, 'r') as temp:
        temps = temp.readlines()
        return [temp.strip() for temp in temps]

# 读取url文件
def read_url_file(filename):
    with open(filename, 'r') as temp:
        temps = temp.readlines()
        result = []
        for temp in temps:
            temp = temp.strip('/').strip()
            if temp.startswith('http://') == False or temp.startswith('https://') == False:
                result.append('http://' + temp)
        return result

# 获取代理设置
def get_proxy_config(filename):
    config = configparser.ConfigParser()
    config.read(filename, encoding='utf-8')
    protocol = config.get('proxy', 'protocol')
    host = config.get('proxy', 'host')
    port = config.get('proxy', 'port')
    username = config.get('proxy', 'username')
    password = config.get('proxy', 'password')
    if len(username) > 0:
        return {'http': f'{protocol}://{username}:{password}@{host}:{port}',
                'https': f'{protocol}://{username}:{password}@{host}:{port}'}
    else:
        return {'http': f'{protocol}://{host}:{port}',
                'https': f'{protocol}://{host}:{port}'}

# web存活测试
def web_alive(url, proxies=None):
    try:
        res = requests.get(url, headers={'User-Agent': USER_AGENT[0]}, proxies=proxies, timeout=5)
        if res.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# 日志记录
def log_write(info):
    with open('./spring_log.txt', 'a+', encoding='utf-8') as w:
        w.write(f'[{getLastDate()}] {info}\n')

if __name__ == '__main__':
    proxy = get_proxy_config('./config.ini')
    print(web_alive('http://www.baidu.com', proxy))