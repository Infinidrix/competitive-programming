def tester(func, params):
    param = ""
    for i in params:
        param += i + ", "
    param = param[0:-2]
    print(eval(func+"("+param+")"))

