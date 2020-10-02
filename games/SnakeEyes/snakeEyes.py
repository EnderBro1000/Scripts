import random

n = 100000
rolls = 0
SEcount = 0

random.seed()

while rolls < n:
    roll1 = random.randrange(1, 7, 1)
    roll2 = random.randrange(1, 7, 1)
    if roll1 == 1 and roll2 == 1:
        SEcount += 1
    rolls += 1

print(f'{SEcount} / {rolls}')
SEpercent = (SEcount / rolls) * 100

print(f'{SEpercent}' + '%')