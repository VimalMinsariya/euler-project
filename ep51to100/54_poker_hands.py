from time import thread_time

poker_hierarchy = {0 : 'High Card',1 : 'One Pair', \
                   2 : 'Two Pair', 3 : 'Three of a Kind', \
                   4 : 'Straight', 5 : 'Flush', \
                   6 : 'Full House', 7 : 'Four of a Kind', \
                   8 : 'Straight Flush', 9 : 'Royal Flush'\
                   }
number_tr = dict((r,i) for i,r in enumerate('..23456789TJQKA'))

def poker(player): # player 변수 예시: ['5C', '4D', '2C', '2H', '2S']
    shapes = [shape for number,shape in player] # ['C', 'D', 'C', 'H', 'S']
    numbers = sorted([number_tr[number] for number, shape in player]) # [2,2,2,4,5]
    numbers.reverse() # [5,4,2,2,2]
    flush = len(set(shapes)) == 1
    straight = len(set(numbers)) == 5 and (max(numbers)-min(numbers)) == 4

    def kind(k): # 같은 숫자가 k개인 것들 모음
        return tuple(r for r in numbers if numbers.count(r)==k)

    if straight and flush and numbers[0] == 13: return (9,)
    if straight and flush and numbers[0] != 13: return (8,)+tuple(numbers)
    if kind(4): return (7,)+kind(4)+kind(1)
    if kind(3) and kind(2): return (6,)+kind(3)+kind(2)
    if flush: return (5,)+tuple(numbers)
    if straight: return (4,)+tuple(numbers)
    if kind(3): return (3,)+kind(3)+kind(1)
    if kind(2) and len(kind(2))==4: return (2,)+kind(2)+kind(1)
    if kind(2) and len(kind(2))==2: return (1,)+kind(2)+kind(1)
    return (0,)+tuple(numbers)

with open('poker.txt','r') as f:
    games = f.readlines()

v = 0
N = len(games)
for i in range(N):
    game = games[i].strip('\n').split(' ')
    player1, player2 = game[0:5], game[5:10]
    p1, p2 = poker(player1), poker(player2)
    print("== Game[",i,"] ==")
    print(player1,poker_hierarchy[p1[0]])
    print(player2,poker_hierarchy[p2[0]])
    if p1 > p2:
        v += 1
        print("player1 wins!")
    elif p1 < p2:
        print("player2 wins!")
    else:
        print("This game is tied")
    print("")

print("player1이 이간 횟수", v)
print("")
print("실행시간:", thread_time(),"초")