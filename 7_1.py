# 7.1
# Manual Test
#              x = (a + 4 * c) / (2 * c + a)
# a = 2, c = 4  => (2 + 4 * 4) / (2 * 4 + 2) = 1.8
# a = 3, c = 5  => (3 + 4 * 5) / (2 * 5 + 3) = 13

# [x] 20230223193858 Переделать в input
# [x] 20230223200909 Обернуть в ф.

a = int(input("a = "))
c = int(input("c = "))


def calculate(a, c):
    print("x = (a + 4 * c) / (2 * c + a)")

    x = (a + 4 * c) / (2 * c + a)

    return x


x = calculate(a, c)

print("x =", x)
