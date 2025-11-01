def permutation_recursive(nums: list[int])-> list[list[int]]:
    results: list[list[int]] = []
    if len(nums) == 0:
        return [[]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutation=permutation_recursive(nums.copy())
        for perm in permutation:
            perm.append(n)
        results.extend(permutation)
        nums.append(n)
    return  results

def permute_backtrack(nums: list[int])-> list[list[int]]:

    def backtrack(start: int) -> None:
         if start == len(nums)-1:
             output.append(nums[:])
         else:
             for i in range(start, len(nums)):
                 nums[start], nums[i] = nums[i], nums[start]
                 backtrack(start + 1)
                 nums[start], nums[i] = nums[i], nums[start]

    output: list[list[int]] = []
    backtrack(0)
    return output

if __name__== "__main__":
    import doctest
    result=permutation_recursive([1,2,3])
    print(result)
    doctest.testmod()







