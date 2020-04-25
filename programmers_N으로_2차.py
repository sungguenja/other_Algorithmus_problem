def solution(N,number):
    case = [0,{N}]
    # N과 number가 같다면 실행시킬 필요도 없으니 바로 끝
    if N==number:
        return 1
    else:
        # 회수를 이용할 겸 case안을 이용하기 위해 i로 2,9까지 for문을 돌린다
        for i in range(2,9):
            # 맨 처음은 단순 무식하게 N이 i개 써졌을 경우
            now_case = {int(str(N)*i)}
            # 절반까지만 돌린다 왜냐하면 끝까지 돌 필요가 없기 때문
            for j in range(1,i//2+1):
                for bf_case in case[j]:
                    # 만약 지금 number가 12고 N은 5라하고 i는 4라고 하자
                    # 그러면 1번째 케이스와 3번째 케이스의 조합
                    # 다시 2번째 케이스와 2번째 케이스의 조합만 하면 된다
                    # 따라서 맨 처음과 맨 끝을 한칸씩 땡기면서 조합 생성
                    for af_case in case[i-j]:
                        now_case.add(bf_case+af_case)
                        now_case.add(bf_case*af_case)
                        now_case.add(bf_case-af_case)
                        now_case.add(af_case-bf_case)
                        if af_case != 0:
                            now_case.add(bf_case//af_case)
                        if bf_case != 0:
                            now_case.add(af_case//bf_case)
            # 모든 경우를 다 만들고 와서 number가 있을경우 지금의 반복상태를 리턴해준다
            if number in now_case:
                return i
            # 없으면 지금 케이스를 이용하기 위해 case에 넣어준다
            else:
                case.append(now_case)
        # 8까지 돌았지만 끝나지 않았을 경우 -1을 리턴한다
        return -1