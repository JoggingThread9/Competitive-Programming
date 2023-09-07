# highest number you can't get combining 6,9,20
# num < 50

num = 1

nums = [6, 9, 20]
for i in nums:
    num_plus_6 = i + 6
    num_plus_9 = i + 9
    num_plus_20 = i + 20

    if num_plus_6 in nums:
        pass
    else:
        nums.append(num_plus_6)

    if num_plus_9 in nums:
        pass
    else:
        nums.append(num_plus_9)

    if num_plus_20 in nums:
        pass
    else:
        nums.append(num_plus_20)

    if num_plus_6 > 1000:
        break

count = 0
off_list = []
for i in range(1, 100):
    if i not in nums:
        count += 1
        off_list.append(i)

print("solution", count)
print("last #", max(off_list))
print(sorted(nums))





