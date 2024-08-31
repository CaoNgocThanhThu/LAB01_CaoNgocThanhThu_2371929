# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:30:38 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = int(input("Nhập số giờ thứ nhất: "))
b = int(input("Nhập số phút thứ nhất: "))
c = int(input("Nhập số giây thứ nhất: "))
giaythunhat = a * 3600 + b * 60 + c
d = int(input("Nhập số giờ thứ hai: "))
e = int(input("Nhập số phút thứ hai: "))
f = int(input("Nhập số giây thứ hai: "))
giaythuhai = d *3600 + e * 60 + f
g = int(input("Chọn 1 để cộng hoặc 2 để trừ: "))
# Cộng
giocong = a + d
phutcong = b + e
giaycong = c + f
# Trừ
giotru = a - d
phuttru = b - e
giaytru = c - f
if g == 1:
    print("Kết quả là: ", giaythunhat + giaythuhai)
    print(f"{giocong} giờ {phutcong} phút {giaycong} giây")
elif g == 2:
    print("Kết quả là: ", giaythunhat - giaythuhai)
    print(f"{giotru} giờ {phuttru} phút {giaytru} giây")
else:
    print("Lựa chọn của bạn không hợp lệ")