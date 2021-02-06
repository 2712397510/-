# -*- coding: utf-8 -*-
# @Time    : 2021/2/6/006 11:39
# @Author  : XiaoLanTiao
# @Email   : xiaolantiao@gmail.com
# @File    : demo1.py
# @Software: PyCharm
# 等比数列
aq1 = int(input('请输入等比数列的首项\n'))
q = int(input('请输入等比数列的公比\n'))
# 等差数列
ad1 = int(input('请输入等差数列的首项\n'))
d = int(input('请输入等差数列的公差\n'))
# 差比数列的参数
a = d*aq1
b = (ad1-a)
A = a/aq1
B = (b-A)/(q-1)
C = -B
print('前n项和为','(',str(A),'n','+',str(B),')*'"q**n","+",C,"（注：'**'为乘方的意思）")
input('请按回车键退出')