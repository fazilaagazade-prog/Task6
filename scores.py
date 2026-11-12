scores = [78, 92, 65, 88, 100, 54, 91, 73]

total = 0
high_count = 0
highest = scores[0]

for score in scores:
    total += score
    if score >= 90:
        high_count += 1
    if score > highest:
        highest = score

average = total / len(scores)

print("Ballarin cemi:", total)
print("Orta bal:", average)
print("90 və yuxari bal alanlarin sayi:", high_count)
print("En yuksek bal:", highest)