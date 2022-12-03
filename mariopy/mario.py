s = 1
while s == 1:
    h = input("Height: ")
    if not h.isnumeric():
        continue
    elif int(h) > 8:
        continue
    elif int(h) < 1:
        continue

    height: int = int(h)
    width = height * 2
    for i in range(height):
        for j in range(width + 2):
            if j < abs(i - (height - 1)):
                print(" ", end="")
            elif j == height:
                print("  ", end="")
            elif j <= height + i + 1:
                print("#", end="")
        print()
    break