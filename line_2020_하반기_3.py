def solution(n):
    answer = []
    minimum_cnt = 99999999
    minimum_case = 0
    def find(now,cnt=0):
        nonlocal minimum_cnt,minimum_case,answer
        if cnt>=minimum_cnt:
            return
        if now<10:
            if minimum_cnt>cnt:
                minimum_cnt = cnt
                minimum_case = now
                answer = [minimum_cnt,minimum_case]
            return
        
        devide_number = 1
        while devide_number<now:
            head,foot=now//(devide_number*10),now%(devide_number*10)
            if foot<devide_number and foot != 0:
                devide_number *= 10
                continue
            devide_number *= 10
            find(head+foot,cnt+1)
    find(n)
    return answer
print(solution(73425))
print(solution(10000))