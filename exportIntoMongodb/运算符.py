# -*- coding: UTF-8 -*-
# import random
# import copy
# a = 10
# b = 20
# c = 0
# # 算术运算符
# print(a + b)  # 加法 30
# print(a - b)  # 减法 -10
# print(a * b)  # 乘法 200
# print(a / b)  # 除法 0.5
# print(b % a)  # 取模 0
# print(3 // 2)  # 取整除 舍入 1
#
# # 比较运算符
# print(a == b)  # 判断是否相等  False
# print(a != b)  # 判断是否不等 True
# # print(a <> b) # 判断是否不等,已废除
# print(a > b)  # False
# print(a < b)  # True
# print(a <= b)  # True
# print(a >= b)  # False
#
# # 赋值运算符
# # a = b
# # print(a) # 20
# # a += 20
# # print(a)  # 30
# # a -= 20
# # print(a)  # -10
# # a *= 20
# # print(a)  # 200
# # a /= 20
# # print(a)  # 0.5
# # a %= 20
# # print(a)  # 10
# # a **= 2  # 幂等于
# # print(a)  # 100
# # a //= 20  # 取整除
# # print(a)  # 0
#
# # 位运算符
# # 按位运算符是把数字看作二进制来进行计算的
# aa = 60  # 0011 1100
# bb = 13  # 0000
# # a & b  a | b   a ^ b   ~a   a << b    a >> b
#
# # 逻辑运算符 与 或 非
# # and or not
# print(1 and 0)  # a & b a为真,值为b;a为假,值为a   0
# print(1 and 2)  # 同上,两者全为真,则取最后一个数的值 2
#
# print(3 or 0)  # 若a or b,a为真,则值为真,a为假则值为b  3
# print(4 or 5)  # 若值为真,则为真 4
# print(0 or 4)  # 4
#
# print(not 0)  # True
# print(not 2)  # False
#
# # 成员运算符 包含 和 不包含
# print(2 in [1, '23', 2])  # True
# print(2 not in [1, 2, 3, 4, 5])  # False
#
# # 身份运算符
# aa = [1, 2, 3, 4, 5]
# bb = aa
# # bb = copy.copy(aa)  # 浅拷贝 只对一层拷贝生效
# print('bb is aa', bb is aa)  # bb is aa  =>  True
#
# aa = [1, 2, 3, [3, 4, 5], 7]
# bb = copy.copy(aa)
# print('bb is aa', bb is aa)  # bb is aa  =>  False
# bb[3][1] = 5
# print(bb, aa)  # copy属于浅拷贝,虽然不相等,但是修改其中一个,另一个也会跟着变化!!!
# cc = copy.deepcopy(aa)  # 深拷贝
# print('cc is aa', cc is aa)  # cc is aa  =>  False
# cc[3][1] = 6
# print(cc, aa)  # deepcopy属于深拷贝,改变其中一个另一个不会改变!!!
#
#
# # 对类型为list的列表去重,方法汇总
# def uniqueA(params):
# 	return list(set(params)) if type(params) == type([]) else params
# def uniqueB(params):
# 	return {}.fromkeys(params).keys() if type(params) == type([]) else params
# def uniqueC(params):
# 	uniqueList = []
# 	if type(params) == type([]):
# 		for key in params:
# 			if key not in uniqueList:
# 				uniqueList.append(key)
# 	else:
# 		uniqueList = params
# 	return uniqueList
# def uniqueD(params):
# 	resultList = []
# 	if type(params) == type([]):
# 		params = sorted(params)
# 		i = 0
# 		while i < len(params):
# 			if params[i] not in resultList:
# 				resultList.append(params[i])
# 			else:
# 				i+=1
# 	else:
# 		resultList = params
# 	return resultList
# print('去重A', uniqueA([1, 2, 1, 1, 2, 3, 4]))
# print('去重B', uniqueB([1, 2, 1, 1, 2, 3, 4]))
# print('去重C', uniqueC([1, 2, 1, 1, 2, 3, 4]))
# print('去重D', uniqueD([1, 2, 1, 1, 2, 3, 4]))
#
#
# # python随机数
# print(random.random())  # 生成一个0-1之间的随机浮点数 0.4944412344506868
# print(random.uniform(1, 6))  # 生成 [1, 6]之间的随机浮点数 1.3792376410411742
# print(random.randint(1, 6))  # 生成[1, 6]之间的随机整数 6
# print(random.randrange(1, 6, 2))  # 在指定集合[1, 6]中按步数为2的方式随机去一个数 3
# print(random.choice([1, '爱你', '小红', '宝贝']))  # 在随意组合的序列中选出一个值 爱你
# a1 = 'str'
# a2 = 2
# a3 = [1, 2, 3, 4, 5]
# a4 = {a: 1}
# print(type(a1))  # <class 'str'>
# print(type(a2))  # <class 'int'>
# print(type(a3))  # <class 'list'>
# print(type(a4))  # <class 'dict'>
# print(type(a1) == type('1'))  # True
# print(type(a2) == type(1))  # True
# print(type(a3) == type([]))  # True
# print(type(a4) == type({}))  # True
#
# print("你好，世界")
"""
打印菱形、三角形、矩形
使用for循环来实现打印对应的形状
"""

# 打印菱形
# -*- coding: UTF-8 -*-
rows = int(input("输入列数:"))
print("实心菱形上半部分", rows)
for i in range(0, rows):
	for j in range(0, rows - i):
		print(" ", end="")
		j += 1
	for k in range(0, 2 * i - 1):
		print("*", end="")
		k += 1
	print("\n")
	i += 1
	
for l in range(0, rows):
	for m in range(0, l):
		print(" ", end="")
		m += 1
	for n in range(0, 2 * (rows - l) - 1):
		print("*", end="")
		n += 1
	print("\n")
	l += 1
	
	
# 打印其他形状的
# 2021年9月26日18:33:15
