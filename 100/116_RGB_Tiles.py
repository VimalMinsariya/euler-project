ra, rb = 1, 2
ga, gb, gc = 1, 1, 2
ba, bb, bc, bd = 1, 1, 1, 2

for i in range(3,51):
    if i>2:
        ra, rb = rb, ra+rb
    if i>3:
        ga, gb, gc = gb, gc, gc+ga
    if i>4:
        ba, bb, bc, bd = bb, bc, bd, bd+ba

print((rb-1)+(gc-1)+(bd-1))