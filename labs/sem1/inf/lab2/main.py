from random import randint


def task(a):
    def get_s(s):
        if int(a[s[0]] ^ a[s[1]] ^ a[s[2]] ^ a[s[3]]) == 1:
            return s[0] + 1
        return 0

    error = get_s([0, 2, 4, 6]) + get_s([1, 2, 5, 6]) + get_s([3, 4, 5, 6]) - 1
    name = ["r1", "r2", "i1", "r3", "i2", "i3", "i4"]
    if error == -1:
        print("Ошибок нет")
        return
    a[error] = int(not a[error])
    print(f"Ошибка в бите {name[error]}. Сообщение без ошибок: {"".join(list(map(str, [a[2], a[4], a[5], a[6]])))}")


def test():
    print("1. Исходное сообщение: 1010011")
    task(list(map(int, list("1010011"))))
    print("2. Исходное сообщение: 0100110")
    task(list(map(int, list("0100110"))))
    print("3. Исходное сообщение: 1101000")
    task(list(map(int, list("1101000"))))
    print("4. Исходное сообщение: 1010000")
    task(list(map(int, list("1010000"))))
    for i in range(5, 11):
        s = [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]
        print(f"{i}. Исходное сообщение: {"".join(list(map(str, s)))}")
        task(s)


if __name__ == "__main__":
    test()
