import random
from typing import List


def Square(n: int) -> int:
    i: int = 0
    while i < n:
        print('* '*n)
        i += 1
    return n**2


def Line(n: int) -> int:
    print('* '*n)
    return n


def Triangle(n: int) -> int:
    i: int = 0
    a: int = 1
    while i < n:
        print('* ' * a)
        a *= 2
        i += 1

    return (2**n) - 1


def Striangle(n: int) -> int:
    i: int = 1
    while i <= n:
        print('* ' * i)
        i += 1
    return (1 + n) * (n / 2)


Line(4)  # 0.5
Square(4)  # .25
Triangle(4)  # .1
Striangle(4)  # .15

i: int = 0
sum: int = 0
sum_square: int = 0
# variance_list: List[int] = []
while i < 1000:
    rand_i: int = random.randint(1, 100)
    iteration_addition: int = 0
    match rand_i:
        case rand_i if 1 <= rand_i < 50:
            iteration_addition += Line(4)
        case rand_i if 51 <= rand_i < 75:
            iteration_addition += Square(4)
        case rand_i if 76 <= rand_i < 85:
            iteration_addition += Triangle(4)
        case rand_i if 86 <= rand_i < 100:
            iteration_addition += Striangle(4)
    # variance_list.append(iteration_addition)
    sum += iteration_addition
    sum_square += iteration_addition ** 2
    i += 1
average: float = sum / 1000

# variance_sum = 0

# for variance in variance_list:
#     variance_sum += (variance - average) ** 2

print(f'srednia = {average}')

print(f'wariancja = {1/1000 * sum_square - average ** 2}')
