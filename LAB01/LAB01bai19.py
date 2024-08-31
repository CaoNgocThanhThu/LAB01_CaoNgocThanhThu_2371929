# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:10:12 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))
if a <= b and a <= c and a <= d:
    so_nho = a
elif b <= a and b <= c and b <= d:
    so_nho = b
elif c <= a and c <= b and c <= d:
    so_nho = c
else:
    so_nho = d
print("Số nhỏ nhất là: ", so_nho)