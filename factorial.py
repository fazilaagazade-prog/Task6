n = int(input("Ədəd yazın: "))

if n < 0:
    print("Mənfi ədədin faktorialı yoxdur")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! = {result}")