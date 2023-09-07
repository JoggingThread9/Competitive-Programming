# find the minimum amount of moves to get to the end

nums = input()
# input format: A B X Y
nums = nums.split(' ')
nums = list(nums)
for i in range(len(nums)):
    nums[i] = int(nums[i])

start = nums[0]
end = nums[1]

tel1 = nums[2]
tel2 = nums[3]

numLine = [i for i in range(1, end+1)]
# can only move 1 or -1

start_to_end_forward = abs(end - start)
start_to_end_backward = abs(start + end - len(numLine) + 1)

start_to_tel1 = abs(start - tel1)
start_to_tel2 = abs(start - tel2)

tel1_to_end = abs(tel1 - end)
tell2_to_end = abs(tel2 - end)

minimum = start_to_end_forward


if minimum > start_to_end_backward:
    minimum = start_to_end_backward

if start_to_tel1 + tell2_to_end < start_to_tel2 + tel1_to_end:
    if start_to_tel1 + tell2_to_end < minimum:
        minimum = start_to_tel1 + tell2_to_end
else:
    if start_to_tel2 + tel1_to_end < minimum:
        minimum = start_to_tel2 + tel1_to_end

print(minimum)



