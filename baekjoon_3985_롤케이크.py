L = int(input())
bread = [None]*(L+1)
person = int(input())
predict = 0
pre_who = 0
for people in range(1,person+1):
    start_point, end_point = map(int, input().split())
    if predict < end_point - start_point:
        predict = end_point - start_point
        pre_who = people
    for i in range(start_point, end_point+1):
        if bread[i] == None:
            bread[i] = people
        else:
            continue
longest = 0
who = 0
for people in range(1,person+1):
    if longest < bread.count(people):
        longest = bread.count(people)
        who = people

print(pre_who)
print(who)