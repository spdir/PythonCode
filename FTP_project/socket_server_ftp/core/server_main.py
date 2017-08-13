__Author__ = "ZhiChao Ma"

import socketserver
import json
import os

class ServerFtp(socketserver.BaseRequestHandler):
    """服务器端"""
    def __userVerif__(self):
        """用户验证"""
        pass

    def __userhomedir__(self):
        """用户家目录定位"""
        pass

    def handle(self):
        """逻辑处理调用的接口"""
        while True:
           try:
               client_address = self.client_address[0]
               self.data = self.request.recv(1024)
               mgs_dit = json.loads(self.data.decode())
               cmd = mgs_dit['cmd']
               if hasattr(self,'c_'+cmd):
                   func = getattr(self,'c_'+cmd)
                   func(mgs_dit)
           except ConnectionResetError as e:
               print('[ERROR]: 客户端%s已断开%s'%(client_address, e))
               break
           except json.decoder.JSONDecodeError:
               print("客户端%s已断开"%client_address)
               break

    def c_put(self,*args):  #基本功能已实现
        """客户端用户上传文件"""
        self.request.send('yes'.encode('utf-8'))
        mgs_dic = args[0]
        filename = mgs_dic['filename']
        filesize = mgs_dic['filesize']
        if not os.path.isfile(filename):
            cover = 'no'
        else:
            cover = 'yes'
        self.request.send(cover.encode('utf-8'))
        recv_cover = self.request.recv(1024).decode()
        if recv_cover == 'y':
            f  = open(filename,'wb')
            local_filesize = 0
            while filesize > local_filesize:
                if filesize - local_filesize > 1024:
                    recv_size = 1024
                else:
                    recv_size = filesize - local_filesize
                data = self.request.recv(recv_size)
                tmp_filesize = len(data)
                f.write(data)
                local_filesize += tmp_filesize
            else:
                f.close()
        else:
            pass

    def c_get(self,*args):  #已实现基本的功能
        """客户端用户下载文件"""
        self.request.send('yes'.encode())
        mgs_dic_server = args[0]
        filename = mgs_dic_server['filename']
        if os.path.isfile(filename):
            filesize = os.stat(filename).st_size
            exist = 'yes'
        else:
            exist = 'no'
        mgs_dic_client = {
            'filesize':filesize,
            'exist':exist,
        }
        self.request.send(json.dumps(mgs_dic_client).encode('utf-8'))
        file_cover_exist = self.request.recv(1024).decode()
        if exist == 'yes' and file_cover_exist == 'yes':
            f = open(filename,'rb')
            for line in f:
                self.request.send(line)
            else:
                ok = self.request.recv(1024)    #防止粘包
                f.close()
        else:
            pass

    def c_cd(self,*args):
        """客户端用户切换目录"""
        pass

    def c_pwd(self,*args):
        """客户端用户查看所处路径"""
        pass

    def c_ls(self,*args):
        """客户端用户查看目录下所有内容"""
        all_list = os.listdir()
        dir_list = []
        file_lsit = []
        unknown_list = []
        for i in all_list:
            if os.path.isfile(i):
                file_lsit.append(i)
            elif os.path.isdir(i):
                dir_list.append(i)
            else:
                unknown_list.append(i)
        all_list_data = {
            'file':file_lsit,
            'dir':dir_list,
            'unknown':unknown_list,
        }
        self.request.send(json.dumps(all_list_data).encode('utf-8'))

if __name__ == "__main__":
    os.chdir(r'D:\test\test')   #修改单引号中的字符串(绝对路径)
    Host, Port = 'localhost',6969
    server = socketserver.ThreadingTCPServer((Host,Port),ServerFtp)
    server.serve_forever()
