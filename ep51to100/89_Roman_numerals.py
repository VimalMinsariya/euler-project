with open('roman.txt','r') as f:
    numbers = f.readlines()

romanNumber = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
numberToRoman = {0:'',
                 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
                 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
                 100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
                 1000:'M', 2000:'MM', 3000:'MMM', 4000:'MMMM',}

def ntor(n):
    digit = 0
    s = ''
    while n > 0:
        n, r = divmod(n,10)
        s = numberToRoman[r*10**digit] + s
        digit += 1
    return s

total = 0

for number in numbers:
    number = number.strip('\n')
    length = len(number)
    s = 0
    for i in range(length-1):
        if romanNumber[number[i]] >= romanNumber[number[i+1]]:
            s += romanNumber[number[i]]
        else:
            s -= romanNumber[number[i]]
    s += romanNumber[number[-1]]
    s1 = ntor(s)
    d = len(number) - len(s1)
    total += d
    print(number, s, s1, d)

print(total)