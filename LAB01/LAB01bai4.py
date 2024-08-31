# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:48:17 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
N = int(input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10 <= N <= 99:
    ket_qua = (N // 10) + (N % 10)
    print("Kết quả là: ", ket_qua)
else: 
    print("Vui lòng nhập số nguyên dương có 2 chữ số")