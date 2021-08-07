from sys import stdin
input = stdin.readline

def putPerson(left,right):
    last = len(friend_set_list)
    friend_set_list.append(set([left,right]))
    friends[left] = last
    friends[right] = last
    return 2

def putOnePerson(target_set,noob):
    target = friends[target_set]
    friends[noob] = target
    friend_set_list[target].add(noob)
    return len(friend_set_list[target])

def unionTwoSet(left,right):
    left_set = friends[left]
    right_set = friends[right]
    target = left_set
    if left_set < right_set:
        friend_set_list[left_set] = friend_set_list[left_set].union(friend_set_list[right_set])
        friend_set_list[right_set] = None
        for element in friend_set_list[left_set]:
            friends[element] = left_set
        target = left_set
    elif right_set < left_set:
        friend_set_list[right_set] = friend_set_list[right_set].union(friend_set_list[left_set])
        friend_set_list[left_set] = None
        for element in friend_set_list[right_set]:
            friends[element] = right_set
        target = right_set

    return len(friend_set_list[target])

for _ in range(int(input())):
    friends = {}
    friend_set_list = []
    for t in range(int(input())):
        left,right = map(str,input().split())
        left_trigger = friends.get(left)
        right_trigger = friends.get(right)
        if left_trigger == None and right_trigger == None:
            print(putPerson(left,right))
        elif left_trigger == None and right_trigger != None:
            print(putOnePerson(right,left))
        elif left_trigger != None and right_trigger == None:
            print(putOnePerson(left,right))
        else:
            print(unionTwoSet(left,right))