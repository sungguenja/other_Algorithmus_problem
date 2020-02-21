def solution(nums):
    X = len(nums)//2
    category = list(set(nums))
    if X>=len(category):
        return len(category)
    return X
    