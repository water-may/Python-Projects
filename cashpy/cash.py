a = 1
b = 5
c = 10
d = 25
coin = 0

j = 1
while j == 1:
    cash = input("Change owed: ")
    if cash.isalpha() or cash == "":
        continue
    y = float(cash)
    y = round(y)
    y = str(y)
    if not y.isnumeric():
        continue
    break
cash = float(cash)

cash = round(100.0 * cash)

i: int = 1
while i == 1:
    if (cash / d) >= 1:
        cash = cash - d
        coin = coin + 1
        continue
    elif (cash / c) >= 1:
        cash = cash - c
        coin = coin + 1
        continue
    elif (cash / b) >= 1:
        cash = cash - b
        coin = coin + 1
        continue
    elif (cash / a) >= 1:
        cash = cash - 1
        coin = coin + 1
        continue
    elif cash < 1:
        break

print(coin)
