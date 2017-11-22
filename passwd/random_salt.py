# -*- coding:utf-8 -*-
import random,string
def getsalt(chars = string.letters+string.digits):
    return random.choice(chars)+random.choice(chars)
salt = getsalt()
print(salt)
