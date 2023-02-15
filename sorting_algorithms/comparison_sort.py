a=0
b=5
c=0
order = [0, 0, 0]

if a > b:
    order[1] = a
    order[2] = a
    order[0] = b
else:
    order[1] = b
    order[2] = b
    order[0] = a

if order[1] < c:
    order[2] = c
else:
    order[1] = c
    if order[0] > order[1]:
        temp = order[1]
        order[1] = order[0]
        temp = order[0]

print(order)
