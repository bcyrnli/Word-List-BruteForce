#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:27:58 2021

@author: bcyrnli
"""
from ittertools import product
import string

min_len = int(input("minimum değer gir"))
max_len = int(input("maximum değer gir"))
counter = 0
charater = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("wordlist.txt", 'w')

for i in range(min_len,max_len+1):
    for j in product(charater,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter+=1
print("Wordlist ".format(counter))
        