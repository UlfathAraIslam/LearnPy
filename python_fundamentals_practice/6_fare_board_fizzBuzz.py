def fare_announcements(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('RapidExpress')
        elif i % 3 == 0:
            result.append("Local")
        elif i % 5 == 0:
            result.append("Express")
        else:
            result.append(str(i))
    return result
print(fare_announcements(15))
