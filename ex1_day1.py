# -*- coding: utf-8 -*-

# I/O - input/output

################ 0. input ############
# Note:  raw_input is not defined in Python3
# name = input()
# print('My name is', name)
# print(type(name))

# print('0x786 = ', 0x786)
# print('1e9 = ', 1e9)

################ 1. \ ####################
# use '\' to print single quote
# print('I\'m \"OK\"')
# print(r'\\\t\\')
# print('\\\t\\')

# print(""" djkd
# 	shjshkjs
# 	sjkhskjhsk """)


############## 2. logic operator ###############
# Priority: from right to left
# not > and = or
# Different from C/C++: the return value is not a boolean value
# print(not 3 or 8)		# 8
# print(2 and 7)			# 7
# print(2 and 4 or 5)	  	# 4


############## 3. variable ################
# store 'ABC' in the memory, then let a point to this memory location
# a = 'ABC'
# b = a
# let a point to another new memory location
# a = 'abc'
# print('a = ', a)
# print('b = ', b)

# print('测试中文输入法')

############## 4. format string #########
print('My name is %s, and age is %d' % ('Tom', 23))
print('Your name is {0}, and age is {1}'.format('Tom', 23))
