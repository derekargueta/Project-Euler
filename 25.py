
nums = [1, 1]
i = 3
while True:
    new_num = nums[i-2] + nums[i-3]
    nums.append(new_num)
    if len(str(new_num)) == 1000:
        print(i)
        break
    i += 1
