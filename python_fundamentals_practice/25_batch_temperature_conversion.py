# F = C × 9/5 + 32

def convert_all_temps(celsius_list):
    return list(map(lambda c: round(c * 9 / 5 + 32, 1), celsius_list))
print(convert_all_temps([0, 20, 37]))