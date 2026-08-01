def convert_and_print(amount_str, rate):
    amount = int(amount_str.replace(",",""))
    converted = amount * rate
    f_version = f"Amount: ¥{converted:.2f}"
    format_version = "Amount: ¥{:.2f}".format(converted)
    exceeds_threshold = converted > 1000
    return f_version, format_version, exceeds_threshold
print(convert_and_print("1,000", 1.25))
