def solution(brown, yellow):
    core_brown = (brown - 4)//2
    for i in range(1,core_brown):
        j = core_brown - i
        if i > j:
            break
        if i * j == yellow:
            return [j+2,i+2]