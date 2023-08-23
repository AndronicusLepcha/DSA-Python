def guess(nums, m, key):
    if nums[m] == key:
        return 0
    elif nums[m] > key:
        return -1
    else:
        return 1

nums = [20, 30, 40, 50, 60]

l = 0
r = len(nums) - 1

key = 40

while l <= r:
    m = (l + r) >> 1
    if guess(nums, m, key) == 0:
        print("Key found at index", m)
        break  # Key is found, so exit the loop
    elif guess(nums, m, key) == -1:
        r = m - 1
    else:
        l = m + 1
