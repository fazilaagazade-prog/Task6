temperatures = [-3, 2, 8, 15, 22, 27, 31]

for day, temp in enumerate(temperatures, start=1):
    if temp < 0:
        weather = "Şaxta"
    elif temp < 10:
        weather = "Soyuq"
    elif temp < 20:
        weather = "Mülayim"
    elif temp < 30:
        weather = "İsti"
    else:
        weather = "Çox isti"
    print(f"{day}-ci gün: {temp}° → {weather}")