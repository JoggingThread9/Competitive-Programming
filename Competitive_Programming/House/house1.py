min = 3
max = 10**5


def main(start, end):
    nums = 0
    for n in range(start, end+1, 1):
        if min <= n <= max:
            if n % 2 == 0:
                nums += 1

    return nums


print(main(1, 100))


