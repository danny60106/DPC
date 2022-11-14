# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:29:24 2018

Find the longest word that has at least 3 counts
"""
word_dict = {'Programming': 3,'Calculus': 2, 'English': 5, 'Discrete Math': 8}
freq_dict = {k:v for k,v in word_dict.items() if v >= 3}
print(freq_dict)

# sorted() takes a list (or tuple, dict) as an argument and returns a new sorted list.
#l_sorted = sorted(freq_dict.items(), key=lambda x: len(x[0]), reverse=True)
# Sorted by key length
l_sorted = sorted(freq_dict, key=lambda x: len(x), reverse=True)
l_sorted = sorted(freq_dict, key=len, reverse=True)

# Sorted by key value
v_sorted = sorted(freq_dict, key=freq_dict.get, reverse=True) # value-based sorting

print()
print("Sorted by key length: ")
print(l_sorted)
print()
print("Sorted by key value: ")
print(v_sorted)

