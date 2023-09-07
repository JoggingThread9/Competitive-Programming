# a <= b <= c

# numbers represent a, b, c, a+b, b+c, a+c
input = [2, 2, 11, 4, 9, 7, 9]
# output a = 2, b = 2, c = 7


def check(inList, outList):
    for num in inList:
        if num not in outList:
            return False
    return True


for i in range(len(input)):
    a = input[i]
    for j in range(len(input)):
        if j != i:
            b = input[j]
        else:
            break
        for k in range(len(input)):
            output = []

            if k != i and k != j:
                c = input[k]
                if a <= b <= c:
                    output.append(a)
                    output.append(b)
                    output.append(c)
                    output.append(a + b)
                    output.append(b + c)
                    output.append(c + a)
                    output.append(a + b + c)

                    if check(input, output):
                        print(f'a = {a} b = {b} c = {c}')





