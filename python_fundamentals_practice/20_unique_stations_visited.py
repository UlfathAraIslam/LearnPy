'''
1. Create an empty set seen.
To remember which stations have already appeared.

2. Create an empty list result.
To store the unique stations in their original order.

3. Loop through each station in log.
To check every station one by one.

4. If the station is not in seen:
      - Add it to seen.
Mark it as visited.
      - Add it to result.
Keep its first occurrence.

5. Otherwise, skip it.
Avoid duplicates.

6. Return result.
It contains the unique stations in first-seen order.

'''

def unique_stations(log):
    seen = set()
    result = []
    for station in log:
        if station not in seen:
            seen.add(station)
            result.append(station)
    return result
print(unique_stations(["Kusatsu", "Kyoto", "Kyoto", "Osaka", "Kusatsu", "Osaka"])
)