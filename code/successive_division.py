def func(a, b):
    """
    辗转相除 求最大公约数
    """
    print(a, b)
    if b == 0: return a
    m = a % b
    return func(b, m)  # (b, a % b)


print(func(30, 18))
print(func(75, 165))
