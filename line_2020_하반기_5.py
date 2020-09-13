def solution(cards):
    answer = 0
    drow = 'drow'
    win = 'win'
    lose = 'lose'
    black = 'black'
    while cards != []:
        result = None
        try:
            player = [cards[0],cards[2]]
            dealer = [cards[1],cards[3]]
            cards = cards[4:]
        except IndexError:
            break
        if player.count(1) == 1:
            if player[0] == 1:
                if player[1] < 10:
                    player_sum = 11 + player[1]
                else:
                    player_sum = 21
            elif player[1] == 1:
                if player[0] < 10:
                    player_sum = 11 + player[0]
                else:
                    player_sum = 21
        elif player.count(1) == 2:
            player_sum = 12
        else:
            player_sum = 0
            for i in range(2):
                if player[i]>10:
                    player_sum += 10
                else:
                    player_sum += player[i]
        
        if dealer.count(1) == 1:
            if dealer[0] == 1:
                if dealer[1] < 10:
                    dealer_sum = 11 + dealer[1]
                else:
                    dealer_sum = 21
            elif dealer[1] == 1:
                if dealer[0] < 10:
                    dealer_sum = 11 + dealer[0]
                else:
                    dealer_sum = 21
        elif dealer.count(1) == 2:
            dealer_sum = 12
        else:
            dealer_sum = 0
            for i in range(2):
                if dealer[i]>10:
                    dealer_sum += 10
                else:
                    dealer_sum += dealer[i]
        
        if player_sum == 21:
            if dealer_sum == 21:
                result = drow
            else:
                if dealer_sum >= 17:
                    result = black
                else:
                    trigger = True
                    while len(cards) >= 1 and trigger:
                        now_card = cards.pop(0)
                        asdf = False
                        if now_card == 1:
                            if dealer_sum + 11 > 21:
                                asdf = True
                            elif dealer_sum + 11 == 21:
                                result = drow
                            elif 17 <= dealer_sum + 11 < 21:
                                result = black
                                trigger = False
                            if asdf:
                                if dealer_sum + now_card < 17:
                                    dealer_sum += now_card
                                else:
                                    trigger = False
                                    result = black
                        elif now_card>=10:
                            dealer_sum += 10
                            if dealer_sum>21:
                                result = black
                            elif dealer_sum==21:
                                result = drow
                            elif 17 <= dealer_sum + 11 < 21:
                                result = black
                                trigger = False
                        else:
                            dealer_sum += now_card
                            if dealer_sum>21:
                                result = black
                            elif dealer_sum==21:
                                result = drow
                            elif 17 <= dealer_sum + 11 < 21:
                                result = black
                                trigger = False
        else:
            trigger = 0
            for i in range(2):
                if dealer[i] == 1 or dealer[i] >= 7:
                    trigger = 0
                    break
                elif dealer[i] == 4 or dealer[i] == 5 or dealer[i] == 6:
                    trigger = 1
                else:
                    trigger = 2
            if trigger == 0:
                while len(cards)>=1 and player_sum < 17:
                    now_card = cards.pop(0)
                    if now_card == 1:
                        if player_sum + 11 >= 17:
                            pass
                        else:
                            pass
                    elif now_card>=10:
                        pass
                    else:
                        pass
            elif trigger == 1:
                pass
            else:
                pass

        if result == drow:
            continue
        elif result == win:
            answer += 2
        elif result == lose:
            answer -= 2
        elif result == black:
            answer += 3
    return answer