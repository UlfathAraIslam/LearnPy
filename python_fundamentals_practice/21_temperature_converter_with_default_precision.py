def to_fahrenheit(celsius, decimals=1):
    faherenheit = celsius * 9/5 + 32
    return round(faherenheit,decimals)
print(to_fahrenheit(21.5))
print(to_fahrenheit(21.5, 0))