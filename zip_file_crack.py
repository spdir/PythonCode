# -*- coding: UTF-8 -*-
#使用多线程和接受参数的形式去破解指定的zip文件
#python3 zip_file_cack.py -f GitHub.zip -d dicfile.txt
import zipfile
import optparse
import threading

def extractFile(zFile,password):
  try:
    zFile.extractall(pwd=password.encode())
    print('[+] password = %s' % (password))
  except Exception as e:
    pass
  
def main():
  parse = optparse.OptionParser("usage: usage: python3 zip_file_crack.py " + "-f <zipfile> -d <dirctionary>")
  parse.add_option('-f', dest='zip_name', type='string', help='specify zip file')
  parse.add_option('-d', dest='dict_name', type='string', help='specify dirctionary')
  (options, args) = parse.parse_args()
  if (options.zip_name == None) or (options.dict_name == None):
    print(parse.usage)
    exit(0)
  else:
    zip_name = options.zip_name
    dict_name = options.dict_name
  zFile = zipfile.ZipFile(zip_name)
  passFile = open(dict_name,'r')
  for line in passFile.readlines():
    password = line.strip()
    t = threading.Thread(target=extractFile,args=(zFile,password,))
    t.start()
if __name__ == '__main__':
  main()
