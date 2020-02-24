def solution(N,number):
    case_list = [0,{N}]
    if N==number:
        return 1
    else:
        for i in range(2,9):
            now_case = {int(str(N)*i)}
            for half in range(1,i//2+1):
                for j in case_list[half]:
                    for k in case_list[i-half]:
                        now_case.add(j+k)
                        now_case.add(j*k)
                        now_case.add(j-k)
                        now_case.add(k-j)
                        if j != 0:
                            now_case.add(k//j)
                        if k != 0:
                            now_case.add(j//k)
            if number in now_case:
                return i
            case_list.append(now_case)
        return -1