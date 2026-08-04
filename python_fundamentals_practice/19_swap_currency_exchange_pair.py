def swap_rates(rate_pair):
    buy,sell = rate_pair
    swapped = (sell, buy)
    return swapped,rate_pair
print(swap_rates((150.25, 151.10)))