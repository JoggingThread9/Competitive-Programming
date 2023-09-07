# format: k n w

# k = amount for first banana
# n = amount of money he has
# w = amount of bananas


inputList = input()
# format: k n w
inputList = inputList.split(' ')
inputList = list(inputList)
for i in range(len(inputList)):
    inputList[i] = int(inputList[i])

k = inputList[0]
n = inputList[1]
w = inputList[2]

total = 0

for i in range(1, w+1):
    total += i*k

ans = total - n

print(ans)
# 13
