def makeSet(string):
    alphabet = [chr(i) for i in range(65,91)]
    arr = []
    for i in range(len(string)-1):
        if string[i] in alphabet and string[i+1] in alphabet:
            arr.append(string[i:i+2])
    return arr

def findUnionIntersection(arr1,arr2):
    union_set = []
    intersection_set = []
    
    visit = [True]*len(arr2)
    for i in range(len(arr1)):
        trigger = True
        for j in range(len(arr2)):
            if visit[j] and arr1[i] == arr2[j]:
                union_set.append(arr1[i])
                intersection_set.append(arr2[j])
                visit[j] = False
                trigger = False
                break
        if trigger:
            union_set.append(arr1[i])
    
    for j in range(len(arr2)):
        if visit[j]:
            union_set.append(arr2[j])
    
    return union_set, intersection_set

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str_set1 = makeSet(str1)
    str_set2 = makeSet(str2)
    union_set,intersection_set = findUnionIntersection(str_set1,str_set2)

    if len(union_set) != 0:
        answer = int((len(intersection_set)/len(union_set))*65536)
    else:
        answer = 65536
    return answer