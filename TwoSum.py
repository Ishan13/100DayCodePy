def two_sums(entered, compare):
    seen_num = {}  # Hashmap to store seen numbers and their indices
    for i, num in enumerate(entered):
        complement = compare - num
        if complement in seen_num:
            return [seen_num[complement], i]
        seen_num[num] = i

    return None


nums = [2, 7, 11, 15]
target = 9
result = two_sums(nums, target)
print(result)
