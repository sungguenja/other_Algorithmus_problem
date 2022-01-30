def solution(stones,k):
    answer = 0
    lower_person_count = 1
    higher_person_count = max(stones) + 1

    while lower_person_count <= higher_person_count:
        mid = (lower_person_count + higher_person_count) // 2

        jump = 0
        for stone_durability in stones:
            if stone_durability - mid <= 0:
                jump += 1
            else:
                jump = 0
            
            if jump >= k:
                break
        
        if jump < k:
            lower_person_count = mid + 1
            answer = lower_person_count
        else:
            higher_person_count = mid - 1

    return answer