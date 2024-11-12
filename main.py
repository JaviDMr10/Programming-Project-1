
total_rain = 0.0
total_wind = 0.0
day_count = 0

while True:
    user_input = input("Enter a rain value and the wind speed separated by a space, or '-1.0' to finish: \n")
    inputs = user_input.split()
    if inputs[0] == '-1.0':
        break
    if len(inputs) != 2:
        print("Incorrect value(s), please enter both rain and wind speed separated by a space, or '-1.0' to finish.")
        continue
    
    rain_value = float(inputs[0])
    wind_speed = float(inputs[1])
    total_rain += rain_value
    total_wind += wind_speed
    day_count += 1

if day_count > 0:
    average_rain = total_rain / day_count
    average_wind = total_wind / day_count
    weather_severity = (average_rain * 10) + average_wind

    print(f"The average rain is {average_rain:.1f} inches")
    print(f"The average wind speed is {average_wind:.1f} mph")
    if day_count > 1:
        print(f"The weather severity for these {day_count} readings is {weather_severity:.1f}")
    else:
        print(f"The weather severity is {weather_severity:.1f}")
else:
    print("No data entered")