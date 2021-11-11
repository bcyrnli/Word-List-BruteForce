#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:08:59 2021

@author: bcyrnli
"""

import itertools

chars = 'maserikt'

n=6
ths = open("şifrelerdeneme.txt", "w")


for j in itertools.product(chars,repeat=n):
        word = "".join(j)
        ths.write(word)
        ths.write('\n')
        
    
        print (''.join(j))
