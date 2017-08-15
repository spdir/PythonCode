__Author__ = "ZhiChao Ma"

import socket
import os
import json
import shutil
import sys
import getpass
import hashlib

class ClientFtp(object):
    """客户端"""
    def __init__(self):
        """初始化连接"""
        self.client = socket.socket()
        self.server_ip = input("Please enter server ip address>> ").strip()
        self.port = 6969

    def __connect__(self):
        """生成一个连接实例"""
        self.client.connect((self.server_ip,self.port))

    def __login__(self):
        """用户登录验证,验证次数超过3次自动退出程序"""
        pass

    def __interactive__(self):
        """用户交互"""
        print("登陆成功")
        while True:
            cmd_inp = input(">>> ").strip()
            if len(cmd_inp) == 0:continue
            cmd = cmd_inp.split()[0]
            if hasattr(self,'cmd_'+cmd):
                func = getattr(self,'cmd_'+cmd)
                func(cmd_inp)
            else:
                print("输入的语法错误，请重新输入，您可以使用'help'命令进行帮助提示")

    def cmd_help(self,*args):
        """命令操作帮助"""
        help_cmd = """
     ------------------------------------------[帮助信息]--------------------------------------------
      1. ls    "查看当前目录下的所有内容";                         
      2. pwd    "查看当前所处的绝对路径";
      3. cd [../]    "cd 切换到用户根目录, cd .. 切换到上一层目录";
      4. put [filename]    "上传文件";
      5. get [filename]    "下载文件";
      6. dir    "查看本地当前目录下的所有内容";
      7. cdl    "切换本地目录";
      8. pwdl   "查看本地所处的完整路径";
      9. rm "删除服务器用户当前目录的文件或文件夹 rm filename/dirname";
      10. rml   "删除客户端用户当前目录的文件或文件夹 lrm filename/dirname";
      11. mkdir "用户在家目录中创建目录, mkdir dirname...";
      13. rename "重命名用户家目录中的文件或文件夹名称  rename filename/dirname";
      12. exit   "退出程序"
     ------------------------------------------------------------------------------------------------
            """
        print(help_cmd)

    def cmd_put(self, *args):   #基本功能已实现
        """向服务器上传文件"""
        cmd_data = args[0].split()
        if len(cmd_data) > 1:
            filename = cmd_data[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    'cmd': 'put',
                    'filename': filename,
                    'filesize': filesize,
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                cover_recv = self.client.recv(1024)
                cover = json.loads(cover_recv.decode())
                if cover:
                    cover_inp = input("文件%s已存在,是否覆盖 y/n: "%filename)
                    if cover_inp == 'y':
                        cover_to = True
                    else:
                        cover_to =False
                else:
                    cover_to = True
                self.client.send(json.dumps(cover_to).encode('utf-8'))
                if cover_to:
                    f = open(filename, 'rb')
                    for line in f:
                        self.client.send(line)
                    else:
                        print("文件%s上传成功"%filename)
                        f.close()
                else:
                    pass
            else:
                print("指定的文件%s不存在"%filename)
        else:
            pass

    def cmd_get(self,*args):    #基本功能已实现
        """服务器:下载文件"""
        cmd_data = args[0].split()
        if len(cmd_data) > 1:
            filename = cmd_data[1]
            mgs_dic = {
                'cmd':'get',
                'filename':filename,
            }
            self.client.send(json.dumps(mgs_dic).encode('utf-8'))
            self.client.recv(1024)  #防止粘包
            file_server_recv_data = self.client.recv(1024).decode()
            file_server_data = json.loads(file_server_recv_data)
            file_size = file_server_data['filesize']
            file_exist = file_server_data['exist']
            if file_exist == 'yes':
                file_cover_exist = ''
                if os.path.isfile(filename):
                    exist = input("当前目录中文件%s已存在,是否覆盖 y/n: "%filename)
                    if exist == 'y':
                        file_cover_exist = 'yes'
                    else:
                        file_cover_exist = 'no'
                elif os.path.isfile(filename):
                    file_cover_exist = 'yes'
                self.client.send(file_cover_exist.encode('utf-8'))
                if file_cover_exist == 'yes':
                    f = open(filename, 'wb')
                    local_file_size = 0
                    while file_size > local_file_size:
                        if file_size - local_file_size > 1024:
                            recv_size = 1024
                        else:
                            recv_size = file_size - local_file_size
                        data = self.client.recv(recv_size)
                        tmp_file_size = len(data)
                        f.write(data)
                        local_file_size +=tmp_file_size
                    else:
                        print("文件%s下载成功"%filename)
                        f.close()
                else:
                    pass
            elif file_exist == 'no':
                print("请求的文件%s不存在"%filename)
        else:
            pass

    def cmd_ls(self,*args):
        """服务器:列出当前目录下的所有内容"""
        cmd_dic = {
            'cmd':'ls',
        }
        self.client.send(json.dumps(cmd_dic).encode('utf-8'))
        data = self.client.recv(1024).decode()
        all_dir_data = json.loads(data)
        dir_list = all_dir_data['dir']
        file_list = all_dir_data['file']
        unknown_list = all_dir_data['unknown']
        print("Server:当前目录下的所有内容(f:file/d:dir/-:unknown):")
        for file in file_list:
            print("f: %s"%file)
        for dir in dir_list:
            print('d: %s'%dir)
        for unknown in unknown_list:
            print('- :%s'%unknown)

    def cmd_cd(self,*args):
        """服务器:切换目录"""
        pass

    def cmd_rm(self,*args):
        """服务器:删除用户家目录的文件"""
        cmd_data=args[0].split()
        if len(cmd_data) > 1:
            filename = cmd_data[1]
            cmd_dic = {
                'cmd':'rm',
                'filename':filename,
            }
            self.client.send(json.dumps(cmd_dic).encode('utf-8'))
            exist_file_data_recv = self.client.recv(1024)
            exist_file_data = json.loads(exist_file_data_recv.decode())
            filetype= exist_file_data['filetype']
            file_exist = exist_file_data['exist']
            really_rm = ''
            if file_exist == 'y' and filetype == 'f':
                really_rm = input("是否删除文件%s y/n:"%filename)
            elif file_exist == 'y' and filetype == 'd':
                really_rm = input("是否删除文件夹%s y/n"%filename)
            else:
                print("[Error] 指定参数%s不存在" % filename)
                pass
            if really_rm == 'y':
                self.client.send(really_rm.encode('utf-8'))
            else:
                pass
        else:
            pass

    def cmd_pwd(self,*args):
        """服务器：查看当前所处的目录"""
        pass

    def cmd_dir(self,*args):
        """客户端：查看本地目录下所有的内容"""
        all_dir_data = os.listdir()
        print("Client:当前目录下的所有内容(f:file/d:dir/-:unknown):")
        for i in all_dir_data:
            if os.path.isfile(i):
                print('f: %s'%i)
            elif os.path.isdir(i):
                print('d: %s'%i)
            else:
                print('- ', i)

    def cmd_cdl(self,*args):
        """客户端：本地切换目录"""
        cmd_data = args[0].split()
        if len(cmd_data) > 1:
            pwd = os.getcwd()
            dir_com = cmd_data[1]
            if dir_com == '..' or dir_com == '../':
                cd_dir = os.path.dirname(pwd)
                os.chdir(dir_com)
            else:
                cd_dir = os.path.join(pwd,dir_com)
                if os.path.isdir(cd_dir):
                    os.chdir(cd_dir)
                else:
                    print('路径不存在')

    def cmd_pwdl(self,*args):
        """客户端：查看本地所处的目录"""
        pwd = os.getcwd()
        print("Client:当前工作目录位于:")
        print(pwd)

    def cmd_rml(self,*args):
        """客户端:删除用户家目录的文件"""
        cmd_data = args[0].split()
        if len(cmd_data) > 1:
            filename = cmd_data[1]
            if os.path.isfile(filename):
                really_rm = input("是否删除%s文件 y/n:"%filename)
                if really_rm == 'y':
                    os.remove(filename)
                else:
                    pass
            elif os.path.isdir(filename):
                really_rm = input("是否删除%s文件夹 y/n:"%filename)
                if really_rm == 'y':
                    shutil.rmtree(filename)
                else:
                    pass
            else:
                print("[Error] 指定参数%s不存在"%filename)
        else:
            pass

    def cmd_mkdir(self,*args):
        """服务端创建文件夹"""
        cmd_data = args[0].split()
        if len(cmd_data) > 1:
            dir_name = cmd_data[1]
            data_dic = {
                'cmd':'mkdir',
                'dir_name':dir_name,
            }
            self.client.send(json.dumps(data_dic).encode('utf-8'))
            exist_recv = self.client.recv(1024).decode()
            if exist_recv == 'y':
                really_mk = input("指定%s已存在是否覆盖(覆盖可能造成文件丢失) y/n:"%dir_name)
                self.client.send(really_mk.encode('utf-8'))
            else:
                pass
        else:
            pass

    def cmd_rename(self,*args):
        """服务端:重命名文件名"""
        cmd_data = args[0].split()
        if len(cmd_data) > 2:
            old_name = cmd_data[1]
            new_name = cmd_data[2]
            cmd_dic = {
                'cmd':'rename',
                'old_name':old_name,
                'new_name':new_name,
            }
            self.client.send(json.dumps(cmd_dic).encode('utf-8'))
            exist_recv = self.client.recv(1024)
            exist = json.loads(exist_recv.decode())
            if exist == 'y':
                pass
            else:
                print("指定文件%s不存在"%old_name)
        else:
            pass

    def cmd_exit(self,*args):
        """用户退出"""
        exit('Bye')
