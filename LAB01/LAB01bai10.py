# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:25:03 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
N = int(input("Nhập biển số xe của bạn: "))
if 1000 <= N < 10000:
    a = N % 1000
    b = a % 100
    c = b % 10
    so_nut = N // 1000 + a // 100  + b // 10 + c % 10
    ket_qua = (so_nut // 10) + (so_nut % 10)
else:
    so_nut = "Biển số không hợp lệ, mời bạn nhập biển 4 số"
print("Biển số của bạn có số nút là: ", ket_qua)
 
    
