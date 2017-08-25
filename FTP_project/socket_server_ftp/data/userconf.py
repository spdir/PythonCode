__Author__ = "ZhiChao Ma"

def usersdata():
    """解析用户文件的信息"""
    with open('user','r') as f:
        usersdata_dic = {}
        for i in f:
            user_info_list = i.split('::')
            key_user_name = user_info_list[0]
            values_user_pwd_path_list =  [user_info_list[1],user_info_list[2]]
            usersdata_dic[key_user_name] = values_user_pwd_path_list
    return usersdata_dic
