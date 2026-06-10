'''
START
   |
   v
Create city list
   |
   v
Create season list
   |
   v
Create 3D weather list
   |
   v
Set highest rainfall variables
   |
   v
Start city while loop
   |
   v
Reset:
hottest_temp
hottest_season
total_rainfall
   |
   v
Start season while loop
   |
   v
Get temperature
Get humidity
Get rainfall
   |
   +--> Print weather data
   |
   +--> Add rainfall
   |
   +--> Check hottest season
   |
   v
Next season
   |
   v
Print hottest season
   |
   +--> Check highest rainfall city
   |
   v
Next city
   |
   v
Print city with highest rainfall
   |
   v
END
'''



# Step 1: Store city names
cities = ["Tokyo", "Osaka", "Kyoto"]


# Step 2: Store season names
seasons = ["Spring", "Summer", "Autumn", "Winter"]


# Step 3: Create 3D weather list
# weather[city][season][measurement]

# Measurement:
# [0] = temperature
# [1] = humidity
# [2] = rainfall

weather = [

    [   # Tokyo

        [18, 60, 120],   # Spring
        [34, 80, 180],   # Summer
        [22, 65, 140],   # Autumn
        [8, 50, 60]      # Winter
    ],

    [   # Osaka

        [20, 62, 110],
        [36, 82, 170],
        [24, 64, 130],
        [9, 52, 55]
    ],

    [   # Kyoto

        [19, 61, 105],
        [35, 79, 165],
        [23, 63, 125],
        [7, 51, 50]
    ]
]


# Variable to track highest rainfall city
highest_rainfall = 0


# Store city name with highest rainfall
highest_rainfall_city = ""


# Print heading
print("==========================================")
print("WEATHER REPORT")
print("==========================================")

#* WHILE LOOP FOR CITIES

c = 0

while c < len(cities):

    # Print city name
    print("City:", cities[c])


    # Variable to track hottest temperature
    hottest_temp = 0


    # Variable to store hottest season
    hottest_season = ""


    # Variable to calculate total rainfall
    total_rainfall = 0


    #* WHILE LOOP FOR SEASONS

    s = 0

    while s < len(seasons):


        # Get temperature
        temperature = weather[c][s][0]


        # Get humidity
        humidity = weather[c][s][1]


        # Get rainfall
        rainfall = weather[c][s][2]


        # Print weather report
        print(
            seasons[s],
            "| Temp:", str(temperature) + "C",
            "Humidity:", str(humidity) + "%",
            "Rain:", str(rainfall) + "mm"
        )


        # Add rainfall to total rainfall
        total_rainfall = total_rainfall + rainfall


        # Check hottest season
        if temperature > hottest_temp:

            hottest_temp = temperature

            hottest_season = seasons[s]


        # Move to next season
        s = s + 1


    # Print hottest season
    print(f"Hottest season: {hottest_season}({hottest_temp}C)")

    # Check highest rainfall city
    if total_rainfall > highest_rainfall:

        highest_rainfall = total_rainfall

        highest_rainfall_city = cities[c]


    # Move to next city
    c = c + 1

print(
    "City with highest annual rainfall:",
    highest_rainfall_city,
    "(" + str(highest_rainfall) + "mm)"
)