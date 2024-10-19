from re import sub


def task(s):
    return sub(r'(?<![:\d\w])([0-1]\d|2[0-3])(:[0-5]\d){1,2}(?![:\d\w])', '(TBD)', s)


def test1():
    s = "Time: 13:30:25, Other Time: 25:30"
    print('\n=================test1=================')
    print(s)
    print("ans =", "Time: (TBD), Other Time: 25:30")
    print("res =", task(s))


def test2():
    s = "Time: 13:69, Other Time: 12:30"
    print('\n=================test2=================')
    print(s)
    print("ans =", "Time: 13:69, Other Time: (TBD)")
    print("res =", task(s))


def test3():
    s = "Time: 13:40:60, Other Time: 12:61"
    print('\n=================test3=================')
    print(s)
    print("ans =", "Time: 13:40:60, Other Time: 12:61")
    print("res =", task(s))


def test4():
    s = "Time: 113:40:40, Other Time: 12:610"
    print('\n=================test4=================')
    print(s)
    print("ans =", "Time: 113:40:40, Other Time: 12:610")
    print("res =", task(s))


def test5():
    s = "Time: 13:40:40, Other Time: 12:510:40"
    print('\n=================test5=================')
    print(s)
    print("ans =", "Time: (TBD), Other Time: 12:510:40")
    print("res =", task(s))


def test():
    test1()
    test2()
    test3()
    test4()
    test5()


test()
