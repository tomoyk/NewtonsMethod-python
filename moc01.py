#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *

x1 = 5.0

def F(x):
  return x*x-2

def Fd(x):
  # return diff(x*x-2, x)
  return 2*x

while True:
  x2 = x1 - F(x1) / Fd(x1)

  if abs(x2 - x1) < 0.0001:
    break

  x1 = x2

  print(x1)
