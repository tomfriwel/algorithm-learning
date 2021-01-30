

calc_count = 0


def fib(N):
    global calc_count
    calc_count = calc_count + 1
    if N == 1 or N == 2:
        return 1
    return fib(N - 1) + fib(N - 2)


print(fib(20))  # 6765
print("calc count: {0}".format(calc_count))

memo = {}