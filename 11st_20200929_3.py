# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    now_sum = sum(A)
    final_sum = (len(A))*(len(A)+1)//2
    answer = abs(final_sum-now_sum)
    if answer > 1000000000:
        answer = -1
    return answer