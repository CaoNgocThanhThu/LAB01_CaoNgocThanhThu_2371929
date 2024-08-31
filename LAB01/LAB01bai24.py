# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:05:30 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
if 0 <= a <= 23 and 0 <= b <=59 and 0 <= c <= 59:
    print("Giờ, phút, giây của bạn hợp lệ")
    print(f"{a} giờ {b} phút {c} giây")
else:
    print("Giờ, phút giây của bạn không hợp lệ!")