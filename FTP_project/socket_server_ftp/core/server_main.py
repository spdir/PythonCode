__Author__ = "ZhiChao Ma"

import ServerCode
import os


if __name__ == "__main__":
    os.chdir(r'D:\test\test')   #修改单引号中的字符串(绝对路径)
    Host, Port = 'localhost',6969
    server = ServerCode.socketserver.ThreadingTCPServer((Host,Port),ServerCode.ServerFtp)
    print("服务端已启动")
    server.serve_forever()

