from re import findall


def task(s):
    return len(findall(r'=-\{P', s))


def test1():
    print('\n=================test1=================')
    print("==-{P-=-{P{=-{P{{=-{P=-{P{=-{P, 6")
    print("res =", task("==-{P-=-{P{=-{P{{=-{P=-{P{=-{P"))


def test2():
    print('\n=================test2=================')
    print("= - { P=-{P= - { P, 1")
    print("res =", task("= - { P=-{P= - { P"))


def test3():
    print('\n=================test3=================')
    print("======------{{{{{{PPPPPP, 0")
    print("res =", task("======------{{{{{{PPPPPP"))


def test4():
    print('\n=================test4=================')
    print("=-\\{P=-\\{P=-\\{P=-{P=-\\{P=-\\{P, 1")
    print("res =", task("=-\\{P=-\\{P=-\\{P=-{P=-\\{P=-\\{P"))


def test5():
    print('\n=================test5=================')
    print("testingtesting=-{Ptesting=-testing{P, 1")
    print("res =", task("testing testing=-{Ptesting=-testing{P"))


def test():
    test1()
    test2()
    test3()
    test4()
    test5()


test()
