# add up to a multiple of seven

input = [7, 3, 8, 1, 5, 3, 17, 10]
output = 5


ans = []
end = len(input)

for i in range(len(input)):
    nums = []
    for j in input[i:]:
        nums.append(j)
        if sum(nums) % 7 == 0:
            ans.append(len(nums))

print(max(ans))