#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *

# シンボルの設定
x = symbols('x')

# debug設定
DEBUG=false

# 元の関数F(x)
def F(ar_x, C):
  return ar_x**2-C

# 微分した関数F'(x)
def Fd(ar_x):
  return 2*ar_x

# Root計算
def sqrt(num):
  x1 = 10 # 開始点のx座標
  counter = 0; # カウンタ

  while True:
    # 次の項を計算
    x2 = x1 - F(x1, num) / Fd(x1)

    # x2とx1の差が0.000000001を下回った時
    if abs(x2 - x1) < 0.000000001:
      break

    # 次の項(x2)を前の項(x1)へ代入
    x1 = x2

    # カウンタを増加
    counter+=1

    # Debugメッセージ
    if DEBUG:
      print(counter,"-",x1)

  return x1

# メイン関数
if __name__ == '__main__':
  nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
  for num in nums:
    print("√",num,"=",sqrt(num))
