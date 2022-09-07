N = int(input())
card = list(i+1 for i in range(N))

while True:
    if len(card) == 1:
        print(card[0])
        break
    print(card.pop(0))
    card.append(card.pop(0))
