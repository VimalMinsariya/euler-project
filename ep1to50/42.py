import time

start = time.time()

def aton(letter):
    result = ord(letter.lower()) - ord('a') + 1
    return result

words = open('p042_words.txt', 'r').read().split(',')
# words=['"sky"','"ksnnxksu"']

cnt = 0

for word in words:
    sum = 0
    for i in word[1:-1]:
        sum += aton(i)
    test = 1 + (8*sum + 1)**(1/2)
    if test == int(test) and int(test) % 2 == 0:
        cnt += 1

print(cnt)

print(time.time()-start)