import os
import sys

# 请在此输入您的代码
#解法一
Lst = [1,1,1]
for i in range(3,20190324):
  new = (Lst[i - 3] + Lst[i - 2] + Lst[i - 1]) % 10000
  Lst.append(new)
  if i == 20190323:
    break
print(new)

#解法二
a, b, c, d = 1, 1, 1, 0
for i in range(4, 20190325):
    d = (a + b + c) % 10000
    a, b, c = b, c, d
print(a, b, c, d)