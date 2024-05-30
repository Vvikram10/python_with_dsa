def next_permutation(nums):
    n = len(nums)
    if n <= 1:
        return

    # Find the rightmost element which is smaller than its next element
    k = -1
    for i in range(n - 1):
        if nums[i] < nums[i + 1]:
            k = i

    # If no such element is found, the array is sorted in descending order
    if k == -1:
        nums.reverse()
        return

    # Find the smallest element on the right of k which is larger than nums[k]
    l = k + 1
    for i in range(k + 1, n):
        if nums[i] > nums[k]:
            l = i

    # Swap the found elements
    nums[k], nums[l] = nums[l], nums[k]

    # Reverse the sequence from k + 1 to end to get the next smallest lexicographic permutation
    nums[k + 1:] = reversed(nums[k + 1:])

# Example usage
arr = [1, 2, 3]
next_permutation(arr)
print(arr)  # Output: [1, 3, 2]
