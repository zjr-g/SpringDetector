import requests, sys, hashlib, json
requests.packages.urllib3.disable_warnings()

def Spring_Check(url,proxies,header_new):
    print("[.] 正在进行Spring的指纹识别")
    Spring_hash = "0488faca4c19046b94d07c3ee83cf9d6"
    Paths = ["favicon.ico", "AabyssZG666"]
    for path in Paths:
        test_url = str(url) + path
        r = requests.get(test_url, timeout=10, verify=False, headers=header_new, proxies=proxies)
        try:
            content_type = r.headers.get("Content-Type", "")
            if "image" in content_type or "octet-stream" in content_type:
                favicon_hash = hashlib.md5(r.content).hexdigest()
                if favicon_hash == Spring_hash:
                    print("[+] 站点Favicon是Spring图标，识别成功")
                    break
            elif r.text and ('timestamp' in r.text):
                print("[+] 站点报错内容符合Spring特征，识别成功")
                break
            else:
                print("[-] 站点指纹不符合Spring特征，可能不是Spring框架")
        except KeyboardInterrupt:
            print("Ctrl + C 手动终止了进程")
            sys.exit()
        except Exception as e:
            print("[-] 发生错误，已记入日志error.log\n")
            f2 = open("error.log", "a")
            f2.write(str(e) + '\n')
            f2.close()

def check(url,proxies,header_new):
    header_new = json.loads(header_new)
    if ('://' not in url):
        url = str("http://") + str(url)
    if str(url[-1]) != "/":
        url = url + "/"
    try:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, timeout=6, verify=False, headers=header_new, proxies=proxies)  # 设置超时6秒
        if r.status_code == 503:
            sys.exit()
        else:
            Spring_Check(url,proxies,header_new)
            return url
    except KeyboardInterrupt:
        print("Ctrl + C 手动终止了进程")
        sys.exit()
    except Exception as e:
        print("[-] URL为 " + url + " 的目标积极拒绝请求，予以跳过！已记入日志error.log", "magenta")
        f2 = open("error.log", "a")
        f2.write(str(e) + '\n')
        f2.close()
        sys.exit()
