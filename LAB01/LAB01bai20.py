# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:19:23 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    so_lon = a
elif b >= a and b >= c:
    so_lon = b
else:
    so_lon = c
print("Số có giá trị lớn nhất là: ", so_lon)