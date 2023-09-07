from math import sqrt

# output = 7.2801098892805

# quadratic formula = ((x2-x1)**2 + (y2-y1)**2)**1/2
x = [1,5,4,7,2]
y = [6,1,8,2,1]

cords = [[1,6], [5,1], [4,8], [7,2], [2,1]]

# [1,6]
# [5,1]
# [4,8]
# [7,2]
# [2,1]

largest = 0


for i in range(len(cords)):
    for j in cords:
        if cords[i] == j:
            pass
        else:
            x1 = cords[i][0]
            y1 = cords[i][1]

            x2 = j[0]
            y2 = j[1]

            d = sqrt((((x2 - x1)**2) + ((y2 - y1) ** 2)))

            if d > largest:
                largest = d

print(largest)
