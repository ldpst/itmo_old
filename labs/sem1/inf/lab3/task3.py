from re import findall


def task(s):
    s = findall(
        r"(<meta name=\"daily_price\" content=([^>]*Bitcoin[^<]*(₽(\d+([,.]\d+)*) RUB)[^<]*)?>)|(<meta name=\"daily_price\" content=([^>]*(₽(\d+([,.]\d+)*) RUB)[^>]*Bitcoin[^<]*)?>)",
        s)
    if len(s) == 0:
        return "Цена не указана"
    else:
        if len(s[0][3]) == 0:
            return s[0][8]
        else:
            return s[0][3]


def test1():
    s = '<meta name="daily_volume" content="В суточным объемом торгов Bitcoin ₽2,56,4566.67 RUB."/> <meta name="daily_price" content="Мы обновляем нашу цену Bitcoin к RUB в режиме реального времени."/> <meta name="daily_price" content=" Цена Bitcoin сегодня составляет ₽456,4566,573.456 RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>'
    print('\n=================test1=================')
    print(s)
    print("ans = 456,4566,573.456")
    print("res =", task(s))


def test2():
    s = '<meta name="daily_volume" content="В суточным объемом торгов Bitcoin цена ₽2,56,4566.67 RUB."/> <meta name="daily_price" content="Мы обновляем нашу цену Bitcoin к RUB в режиме реального времени."/> <meta name="daily_price" content=" Цена Bitcoin сегодня составляет ₽456 RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>'
    print('\n=================test2=================')
    print(s)
    print("ans = 456")
    print("res =", task(s))


def test3():
    s = '<meta name="daily_volume" content="В суточным объемом торгов Bitcoin цена ₽2,56,4566.67 RUB."/> <meta name="daily_price" content="Мы обновляем нашу цену Bitcoin к RUB в режиме реального времени."/> <meta name="daily_volume" content=" Цена Bitcoin сегодня составляет ₽456,467,344.677 RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>'
    print('\n=================test3=================')
    print(s)
    print("ans = Цена не указана")
    print("res =", task(s))


def test4():
    s = '<meta name="daily_volume" content="В суточным объемом торгов Bitcoin цена ₽2,56,4566.67 RUB."/> <meta name="daily_price" content="Мы обновляем нашу цену Bitcoin к RUB в режиме реального времени."/> <meta name="daily_price" content=" Цена Bitcoin сегодня составляет ₽456,1445,356.56 USD."/><meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>'
    print('\n=================test4=================')
    print(s)
    print("ans = Цена не указана")
    print("res =", task(s))


def test5():
    s = '<meta name="daily_volume" content="В суточным объемом торгов Bitcoin цена ₽2,56,4566.67 RUB."/> <meta name="daily_price" content="Мы обновляем нашу цену Bitcoin к RUB в режиме реального времени."/> <meta name="daily_price" content="₽456.1445 RUB - именно столько сегодня стоит Bitcoin."/><meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>'
    print('\n=================test5=================')
    print(s)
    print("ans = 456.1445")
    print("res =", task(s))


def test():
    test1()
    test2()
    test3()
    test4()
    test5()


test()
