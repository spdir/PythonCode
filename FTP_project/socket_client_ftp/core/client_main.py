__Author__ = "ZhiChao Ma"

import ClientCode
import os


if __name__ == "__main__":
    os.chdir(r'D:\test')       #修改单引号中的字符串(绝对路径)
    print(os.getcwd())
    client_connect = ClientCode.ClientFtp()
    try:
        client_connect.__connect__()
    except ClientCode.socket.gaierror as e:
        exit("请求超时，请检查防火墙或服务器的IP地址是否正确")
    client_connect.__interactive__()