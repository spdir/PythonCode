# -*- coding: UTF-8 -*-
#破解UNIX口令密码
import crypt

def testPass(cryptPass):
  salt = cryptPass[0:2]
  dicFile = open('dicfile.txt', 'r')
  if salt == '$6':
    for word in dicFile.readlines():
      word = word.strip()
      cryptWord = crypt.crypt(word,cryptPass)
      if cryptWord == cryptPass:
        print('[+] Found Password:' + word)
        return
    else:
      print('[-] Not Found Password')
      return
  else:
    for word in dicFile.readlines():
      word = word.strip()
      cryptWord = crypt.crypt(word, salt)
      if cryptWord == cryptPass:
        print('[+] Found Password:' + word)
        return
    else:
      print('[-] Not Found Password')
      return

def main():
  passFile = open('passwords.txt','r')
  for line in passFile.readlines():
    if ':' in line:
      user = line.split(':')[0]
      cryptPass = line.split(':')[1].strip()
      print('[*] Cracking Password For: ' + user)
      testPass(cryptPass)

if __name__ == '__main__':
  main()