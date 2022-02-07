amount = int(input())


if amount >= 3600:
    h = (int(amount/3600))
    amount = amount % 3600
else:
    h = 0
if amount >= 60:
    m = (int(amount/60))
    amount = amount % 60
else:
    m = 0
if amount >= 1:
    s = (int(amount/1))
print("{}:{}:{}".format(h, m, s))