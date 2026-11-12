metn = input("Soz və ya cumle yazin: ")

saitler = "aeəıioöuüAEƏIİOÖUÜ"

count = 0

for herf in metn:
    if herf in saitler:
        count += 1

print("Sait sayi:", count)