def countDuplicate(numbers):
    # Write your code here
    set_numbers = set(numbers)
    if len(set_numbers) == len(numbers):
        return 0
    else:
        cnt = 0
        for i in set_numbers:
            if numbers.count(i)>=2:
                cnt+=1
        return cnt