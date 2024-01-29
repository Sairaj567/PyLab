x = int(input("Enter a Number:"))
add = 0
if x > 0:
    while x != 0:
        temp = x
        x -= 1
        add += temp
else:
    print("enter a natural number")

print(add)
