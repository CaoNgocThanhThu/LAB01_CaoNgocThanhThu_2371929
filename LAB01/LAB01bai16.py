# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:04:23 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
ket_qua = gio * 3600 + phut * 60 + giay
print("Kết quả đổi ra giây là: ", ket_qua)