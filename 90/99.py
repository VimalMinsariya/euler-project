import math

lines = open('p099_base_exp.txt').readlines()
max = 0
for line in lines:
    numbers = line.split(',')
    base, exponent = [int(num) for num in numbers]
    value = exponent * math.log10(base)
    if value > max:
        max = value
        line_number = lines.index(line)

print(line_number, lines[line_number])