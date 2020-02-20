stone = int(input())
score = 0
while stone > 0:
    if stone>= 3:
        stone -= 3
        score += 1
    else:
        stone -= 1
        score += 1
if score%2==1:
    print('SK')
else:
    print('CY')