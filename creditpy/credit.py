do = 1

while do == 1:
    card = input("Number: ")
    if len(card) < 10 or len(card) >= 17:
        continue
    break
num = int(card)

if len(card) == 10:
    print("INVALID")
else:
    dev = num / 0.01
    
doo = 1

if len(card) % 2 == 0:
    b = 10
else:
    b = 100
    
su = 0.0
while doo == 1:
    v = num / b
    y = v % 10
    yy = round(y) * 2
    if yy > 10:
        su += 1 + round(yy % 10)
    else:
        su += yy
    
    num = round(v)
    b = 100
    if num == 0:
        break

print(su)
    
if len(card) % 2 == 0:
    b = 100
else:
    b = 10
    
dooo = 1

add = 0.0
while dooo == 1:
    rem = num % b
    if rem >= 10:
        rem = rem % 10
    co = num / b
    add += rem
    num = round(co)
    if round(co) == 0:
        break
    
total = su  + add
print(total)
