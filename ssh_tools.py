# -*- coding: utf8 -*-

import os
import paramiko


class ParamError():
  """参数错误异常"""

  def __init__(self, msg):
    self.message = msg

  def __str__(self):
    return self.message


class Ssh_Sftp():
  def __init__(self, host, port, user, tp, pk):
    """
    :param str host:
    :param int port:
    :param str user:
    :param str tp:
    :param str pk:
    """
    self.ssh_client = self.__init_ssh(host, port, user, tp, pk)
    self.sftp_client = self.__init_sftp(host, port, user, tp, pk)

  def __init_ssh(self, host, port, user, tp, pk):
    """
    初始化ssh连接对象
    :param str host: 主机
    :param int port: 端口
    :param str user: 用户
    :param str tp: p(密码)/k(密钥文件绝对路径)
    :param str pk: 文件或密钥字符串
    :return: ssh conection object
    """
    ssh_client = paramiko.SSHClient()
    try:
      if tp == 'p':
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, port, user, pk)
      elif tp == 'k':
        key = paramiko.RSAKey.from_private_key_file(pk)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, port, user, pkey=key)
      else:
        raise ParamError("ssh connection type Error")
    except Exception as e:
      print(e)
      return None
    else:
      return ssh_client

  def __init_sftp(self, host, port, user, tp, pk):
    """
    初始化sftp连接对象
    :param str host: 主机
    :param int port: 端口
    :param str user: 用户
    :param str tp: p(密码)/k(密钥)
    :param str pk: 文件或密钥字符串
    :return: sftp connection object
    """
    try:
      s = paramiko.Transport((host, port))
      if tp == 'p':
        s.connect(username=user, password=pk)
      elif tp == 'k':
        key = paramiko.RSAKey.from_private_key_file(pk)
        s.connect(username=user, pkey=key)
      else:
        raise ParamError("sftp connection type Error")
    except Exception as e:
      print(e)
      return None
    else:
      return paramiko.SFTPClient.from_transport(s)

  @staticmethod
  def get_local_all_file(root_path):
    """
    获取指定目录下所有文件
    :param str path: 目录路径
    :return: list
    """
    files_list = []
    if not os.path.isdir(root_path):
      return files_list
    root_dir_list = os.listdir(root_path)
    os.chdir(root_path)

    def get_file(path):
      file_list = os.listdir(path)
      for sub_path in file_list:
        if sub_root_path.endswith('.swp') or sub_root_path.startswith('.'):
          continue
        sub_path = os.path.join(path, sub_path)
        if os.path.isfile(sub_path):
          files_list.append(sub_path)
        else:
          get_file(sub_path)

    for sub_root_path in root_dir_list:
      if sub_root_path.endswith('.swp') or sub_root_path.startswith('.'):
        continue
      if os.path.isfile(sub_root_path):
        files_list.append(sub_root_path)
      else:
        get_file(sub_root_path)
    return files_list

  def get_remote_all_file(self, root_path):
    """
    获取远程目录下的所有文件
    :param str root_path: 远程主机的目录
    :return: list
    """
    files_list = []
    try:
      self.sftp_client.stat(root_path)
    except IOError:
      return files_list
    root_dir_list = self.sftp_client.listdir(root_path)
    self.sftp_client.chdir(root_path)

    def get_file(path):
      file_list = self.sftp_client.listdir(path)
      for sub_path in file_list:
        if sub_root_path.endswith('.swp') or sub_root_path.startswith('.'):
          continue
        sub_path = os.path.join(path, sub_path)
        try:
          self.sftp_client.stat(sub_path)
          get_file(sub_path)
        except IOError:
          files_list.append(sub_path)

    for sub_root_path in root_dir_list:
      if sub_root_path.endswith('.swp') or sub_root_path.startswith('.'):
        continue
      try:
        self.sftp_client.stat(sub_root_path)
        get_file(sub_root_path)
      except IOError:
        files_list.append(sub_root_path)
    return files_list

  def sftp_put_file(self, local_file, remote_file):
    """
    文件上传
    :param str local_file: 本地文件
    :param str remote_file: 远程存储文件
    :return : bool
    """
    t1 = remote_file.rstrip('/')
    remote_dir_list = []
    split_list = t1.split('/')
    for i, _ in enumerate(split_list):
      str_path = '/' + '/'.join(split_list[0:i])
      remote_dir_list.append(str_path)
    for remote_dir in remote_dir_list:
      try:
        self.sftp_client.stat(remote_dir)
      except IOError:
        self.sftp_client.mkdir(remote_dir)
    self.sftp_client.put(local_file, remote_file)
    try:
      self.sftp_client.stat(remote_file)
    except IOError:
      pass
    else:
      return True
    return False

  def sftp_get_file(self, remote_file, local_file):
    """
    文件下载
    :param str remote_file: 远程文件
    :param str local_file: 本地存储文件
    :return : bool
    """
    try:
      if self.sftp_client.stat(remote_file):
        self.sftp_client.get(remote_file, local_file)
        if os.path.isfile(local_file):
          return True
    except IOError:
      pass
    return False

  def sftp_get_dir(self, remote_dir, local_dir):
    """
    获取远程目录下的所有文件
    :param str remote_dir: 远程目录
    :param str local_dir: 本地目录
    :return: bool
    """
    try:
      remote_file_list = self.get_remote_all_file(remote_dir)
      for remote_file_path in remote_file_list:
        remote_file = os.path.join(remote_dir, remote_file_path)
        local_file = os.path.join(local_dir, remote_file_path)
        local_file_dir = os.path.dirname(local_file)
        if not os.path.exists(local_file_dir) or not os.path.isdir(local_file_dir):
          os.makedirs(local_file_dir)
        self.sftp_get_file(remote_file, local_file)
    except KeyboardInterrupt:
      return False
    return True

  def sftp_put_dir(self, local_dir, remote_dir):
    """
    将本地目录上传到指定远程目录
    :param str local_dir: 本地目录
    :param str remote_dir: 远程目录
    :return: bool
    """
    try:
      local_file_list = self.get_local_all_file(local_dir)
      for local_file_path in local_file_list:
        local_file = os.path.join(local_dir, local_file_path)
        remote_file = os.path.join(remote_dir, local_file_path)
        self.sftp_put_file(local_file, remote_file)
    except Exception:
      return False
    return True

  def run_command(self, command):
    """
    远程主机运行命令
    :param str command: 命令
    :return : bool
    """
    stdin, stdout, stderr = self.ssh_client.exec_command(command)
    error = stderr.read()
    if error:
      print("run command '%s' Error: --> %s" % (command, error))
    else:
      return True
    return False

  def __del__(self):
    if self.ssh_client:
      self.ssh_client.close()
    if self.sftp_client:
      self.sftp_client.close()
