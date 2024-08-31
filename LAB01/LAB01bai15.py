# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:58:57 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a != b:
    A = math.pow(a,1/3)
    B = math.pow(b,1/3)
    C = ((a + b) / (A + B) -(A*B)) / ((A-B)**2)
    print("Kết quả:",C)
else: 
    print("Biểu thức không xác định")
