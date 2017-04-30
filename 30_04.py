# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:15:21 2017

@author: user
"""

tup = (1,2,3,4)
tup_2 = tup * 2
print (tup_2)


l1 = [2,2,9,1,1,6,3,4,1,7]
list2 = []
def  product_of_list (var_list):
    product = 1
    for item in var_list:
        product *= item
    return product
print (product_of_list (l1))

def find_largest (input_list):
    lardest = input_list[0]
    smallest = input_list[0]
    for element in input_list:
        if element > lardest:
            lardest = element
        if element < smallest:
            smallest = element
    return (lardest, smallest)
print (find_largest (l1))

l1 = [2,2,9,1,1,6,3,4,1,7]
def r_d (list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
print (r_d (l1))


def longer_n (list1, n):
    longer_list = []
    for i in list1:
        if len(i) > n:
            longer_list.append(i)
    return longer_list
print 


