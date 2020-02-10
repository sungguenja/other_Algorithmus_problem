con = True
while con:
    base = int(input('Base = '))
    Height = int(input('Height = '))
    print('Triangle width = {:.1f}'.format(base*Height/2))
    gg = str(input('Continue? '))
    if gg == 'Y':
        con = True
    else:
        con = False