# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:56:36 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
# Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))
print(f"{a}/{b}/{c}")
# Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90)
a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))
y = c % 100
print(f"{a}/{b}/{y}")
# Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20)
a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))
print(f"{c}/{b}/{a}")