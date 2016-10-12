# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:02:39 2016

@author: Ramanuja
"""


def gen_primes(n):
        temp = range(0, n + 1)
        temp[1] = False # Ignore 1
        #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        max_value = int((n)**.5) + 1# i.e. should be less then squrt of n 
        for i in range(2, max_value):
            if temp[i] == False:
                continue
            for j in range(i * 2, len(temp), i):
                if (temp[j] != False):
                    temp[j] = False
        return [i for i in temp if i != False]