amount = int(input())


if amount >= 3600:
    h = amount // 3600
    amount %= 3600
else:
    h = 0
if amount >= 60:
    m = amount // 60
    amount %= 60
else:
    m = 0
if amount >= 1:
    s = amount // 1
print(f"{h}:{m}:{s}")