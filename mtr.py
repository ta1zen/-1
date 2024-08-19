probability_rain = float(input("Вкажіть вірогідність дощу (від 0 до 1): "))

M = {}
outcomes = ["вкрай погано", "погано", "посередньо", "чудово"]

for outcome in outcomes:
    M[outcome] = float(input(f"Вкажіть корисність для результату '{outcome}': "))

forest = probability_rain * M["вкрай погано"] + (1 - probability_rain) * M["чудово"]
home = probability_rain * M["погано"] + (1 - probability_rain) * M["посередньо"]

print(f"Очікувана корисність для пікніка у лісі: {forest}")
print(f"Очікувана корисність для пікніка вдома: {home}")

if forest > home:
    print("Рекомендація: пітити на пікнік у ліс.")
else:
    print("Рекомендація: зробити пікнік вдома.")
