# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 07:42:16 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
hinh = input("Chọn hình vuông (v), chữ nhật (n), tròn (t): ")
if hinh == "v":
        a = float(input("Nhập cạnh của hình vuông: "))
        P = a * 2
        S = a**2
        print("Chu vi là: ", P)
        print("Diện tích là: ", S)
elif hinh == "n":
        b = float(input("Nhập chiều dài của hình chữ nhật: "))
        c = float(input("Nhập chiều rộng của hình chữ nhật: "))
        P = (b + c) * 2
        S = b * c
        print("Chu vi là: ", P)
        print("Diện tích là: ", S)
elif hinh == "t":
        R = float(input("Nhập bán kính R của hình tròn: "))
        P = (R * 2) * 3.14
        S = (R**2) * 3.14
        print("Chu vi là: ", P)
        print("Diện tích là: ", S)
else:
        print("Hình bạn chọn không hợp lệ!!!")
 