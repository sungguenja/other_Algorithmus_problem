def solution(sizes):
    answer = -1
    bigger = []
    smaller = []
    for size in sizes:
        bigger.append(max(size))
        smaller.append(min(size))
    answer = max(bigger)*max(smaller)
    return answer