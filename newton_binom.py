nums = []

for _ in range(int(input())):
    nums.append(int(input()))

for i in range(len(nums) - 1):
    print(nums[i] + nums[i + 1])
