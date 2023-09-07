# y = (n - g) / x, rounded down
# if y < m, y = m
# bessie receives y milk each day

# k * m < n

import math

def main(x, n, k, m):
    if k * m > n:
        return False

    g = 0

    for i in range(k):
        y = math.floor((n-g)/x)
        if y < m:
            y = m

        g += y

    if g > n:
        return True
    return False


n = 10
k = 3
m = 3

print(max(x for x in range(1, n) if main(x, n, k, m)))








