]#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *

# シンボルの設定
x = symbols('x')

# 変数の初期化
x1 = 5
counter = 0;
formula = diff(x**2-2, x)

def F(ar_X):
  return ar_X**2-2

def Fd(ar_x):
  return formula.subs(x, ar_x)

while True:
  x2 = x1 - F(x1) / Fd(x1)

  if abs(x2 - x1) < 0.000000001:
    break

  x1 = x2

  counter+=1
  print(counter,"-",x1)
