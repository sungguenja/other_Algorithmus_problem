from itertools import combinations
from typing import List, Tuple

def compareSum(aDice: List[int], bDice: List[int]) -> Tuple[int, int]:
    aWinCnt = 0
    bWinCnt = 0
    for i in range(0,len(aDice)):
        for j in range(len(bDice)-1,-1,-1):
            if aDice[i] > bDice[j]:
                aWinCnt += j + 1
                break
            if aDice[i] < bDice[j]:
                bWinCnt += 1
    return (aWinCnt, bWinCnt)


def makeSumCase(dice: List[List[int]], pickedLength: int, aDice: List[int], bDice: List[int]) -> Tuple[int, int]:
    A_picked_list = []
    B_picked_list = []
    for i in range(pickedLength):
        A_picked_list.append(dice[aDice[i]])
        B_picked_list.append(dice[bDice[i]])
    print(A_picked_list, B_picked_list)
    if pickedLength == 1:
        return compareSum(A_picked_list[0], B_picked_list[0])
    elif pickedLength == 2:
        return
    elif pickedLength == 3:
        return
    elif pickedLength == 4:
        return
    else:
        return 

def solution(dice: List[List[int]]) -> List[int]:
    winCase = {}
    pickCaseChecker = 0
    diceLength = len(dice)
    diceCombinationCase = list(combinations(range(diceLength), diceLength//2))
    pickCaseLength = len(diceCombinationCase)
    for A_pick_case in diceCombinationCase:
        pickCaseChecker += 1
        if (pickCaseChecker > pickCaseLength / 2):
            break
        B_pick_case = [i for i in range(diceLength) if i not in A_pick_case]
        test = makeSumCase(dice,diceLength//2,A_pick_case,B_pick_case)
        print(A_pick_case,B_pick_case, test)
    answer = []
    return answer
