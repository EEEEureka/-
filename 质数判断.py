while 1:
    test = int(input("请输入要查询的数字："))
    if test > 1:
      for i in range(2,test):
            if test % i == 0:
              print(test,"不是质数")
              print(test // i,"是",test,"的因数")
              break
      else:
        print(test,"是质数")
    else:
        print("输入数据不合法")