# approximate pi
import random

num = 1000000

# N = 100 +- .75
# N = 1000 +- .25
# N = 10000 +- .075

# ex) input : 10000
# ex) output : 3.1436

points = 0

for i in range(num):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    distance = (x*x + y*y)**0.5

    if distance < 1:
        points += 1

pi = 4 * points / num

print(pi)
