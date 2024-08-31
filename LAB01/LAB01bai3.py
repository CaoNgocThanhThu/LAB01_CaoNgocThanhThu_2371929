# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:43:17 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a < 0 and b < 0:
    print("Nhập vào số nguyên dương")
else:
    phan_nguyen = a // b
    print("Kết quả chia lấy phần nguyên: ", phan_nguyen)
    phan_du = a % b
    print("Kết quả chia lấy phần dư: ", phan_du)
