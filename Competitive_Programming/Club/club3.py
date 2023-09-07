rect1 = [6, 6, 8, 8]
rect2 = [1, 8, 4, 9]

x = [rect1[0], rect1[2], rect2[0], rect2[2]]
y = [rect1[1], rect1[3], rect2[1], rect2[3]]

if max(x) - min(x) > max(y) - min(y):
    side = max(x) - min(x)
else:
    side = max(y) - min(y)

print(side**2)

print(max(max(x) - min(x), max(y) - min(y)) ** 2)
