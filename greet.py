students = ["Aysel", "Murad", "Leyla", "Elvin", "Nigar"]
for name in students:
    print(f'Salam {name}!')
    print()
for i, name in enumerate(students, start=1):
    print(f"{i}. Salam {name}!")