password = input("Şifrəni yazın: ")

upper = 0
lower = 0
digits = 0
other = 0

for simvol in password:
    if simvol.isupper():
        upper += 1
    elif simvol.islower():
        lower += 1
    elif simvol.isdigit():
        digits += 1
    else:
        other += 1

print("Böyük hərf:", upper)
print("Kiçik hərf:", lower)
print("Rəqəm:", digits)
print("Digər simvol:", other)

if len(password) > 8 and upper > 0 and lower > 0 and digits > 0 and other > 0:
    print("Şifrə güclüdür")
else:
    print("Şifrə güclü deyil")