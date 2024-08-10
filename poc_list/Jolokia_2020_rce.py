import requests
from time import sleep
requests.packages.urllib3.disable_warnings()

'''


参考链接：

'''

def poc(url, useragent, proxies=None):
    path1 = '/jolokia'
    path2 = '/actuator/jolokia'
    path3 = '/jolokia/list'
    header = {"User-Agent": useragent}


    try:
        re1 = requests.post(url=url + path1, headers=header, timeout=10, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        re2 = requests.post(url=url + path2, headers=header, timeout=10, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        if ((int(re1.status_code) == 200) or (int(re2.status_code) == 200)):
            retest = requests.get(url=url + path3, timeout=10, verify=False, proxies=proxies)
            if retest.status_code == 200 and ('reloadByURL' in str(retest.text) or 'createJNDIRealm' in str(retest.text)):
                return f'[+] 2020 Jolokia-Logback-JNDI-RCE exists. The link: --> {url + path3}'
            else:
                return '[.] No keywords were found in the jolokia/list path, please verify them manually.'
        else:
            return '[-] 2020 Jolokia-Logback-JNDI-RCE not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'

if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))
