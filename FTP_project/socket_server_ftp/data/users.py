__Author__ = "ZhiChao Ma"

import getpass
import hashlib
import os


class UserConf(object):
    """用户的管理"""

    def userinfo(self):
        """处理用户数据文件的内容"""
        with open('user', 'r') as f:
            userinfo_dic = {}
            for info in f:
                userdata = info.split('::')
                userinfo_dic[userdata[0]] = userdata
        return userinfo_dic

    def interaction(self):
        self.help()
        while True:
            choice = input("Please chioce function:")
            if len(choice) == 0:continue
            try:
                function_list = ['help', 'useradd', 'userdel', 'modifyuserinfo','exit']
                index = int(choice) - 1
                choice_func = function_list[index]
            except:
                print("Please try again choice")
                continue
            if hasattr(self,choice_func):
                func = getattr(self,choice_func)
                func()
            else:
                print("Please try again choice")
                continue

    def help(self):
        """help info"""
        print("""
    ---[菜单]---
    1. 查看菜单
    2. 添加用户
    3. 删除用户
    4. 修改用户
    5. exit
    ------------
        """)

    def useradd(self,*args):
        """add user"""
        userinfo_dic = self.userinfo()
        while True:
            username = input("Please enter user name:")
            if username in userinfo_dic:
                print("user [%s] exist" % username)
                continue
            else:break
        while True:
            # userpassword = getpass.getpass("New Password:")
            # again_password = getpass.getpass("Retype new password:")
            userpassword = input("New Password:")
            again_password = input("Retype new password:")
            if userpassword != again_password:
                print("Sorry, passwords do not match")
                continue
            else:
                password_md5 = hashlib.md5(again_password.encode()).hexdigest()
                break
        while True:
            user_home_path = input("Please enter user home path:")
            if not os.path.isdir(user_home_path):
                print('dictory not exist')
                continue
        user_info = "{}::{}::{}".format(username,password_md5,user_home_path)
        with open('user','a') as af:
            af.write('\n'+ user_info)
        print("user %s add successful"% username)

    def userdel(self,*args):
        """delete user"""

    def modifyuserinfo(self,*args):
        """modify user info"""
        pass

    def exit(self):
        """exit procedure"""
        exit("Bye")

if __name__ == "__main__":
    userconf = UserConf()
    userconf.interaction()
