# Question 1

import random
print("Exercise 1")
print("")

daily_temperatures = [random.randint(0, 35) for _ in range(30)]

print("Daily temperatures: ", daily_temperatures)

max_temp = max(daily_temperatures)
min_temp = min(daily_temperatures)
average_temp = sum(daily_temperatures) / len(daily_temperatures)

print("Hottest temperature of the month is: ", max_temp)

print("Coldest temperature of the month is: ", min_temp)

print("The average temperature of the month is: ", average_temp)


# Question 2

print("")
print("")
print("Exercise 2")
print("")

daily_rainfall = [random.randint(0, 10) for _ in range(30)]


print("Daily rainfall: ", daily_rainfall)
print("Daily temperatures: ", daily_temperatures)

worst_day = 1
worst_temp = daily_temperatures[0]
worst_rain = daily_rainfall[0]

for day in range(2, 31):
    temp = daily_temperatures[day - 1]
    rain = daily_rainfall[day - 1]

    if temp < worst_temp and rain > worst_rain:
        worst_day = day
        worst_temp = temp
        worst_rain = rain

print("Worst day is Day", worst_day, "with temperature",
      worst_temp, "and rainfall", worst_rain)


# Question 3

print("")
print("")
print("Exercise 3")
print("")

weekly_temperatures = [
    [random.randint(-1, 10) for _ in range(7)] for _ in range(4)]

print("Weeks Temperatures:", weekly_temperatures)


for week_index, weekly in enumerate(weekly_temperatures, start=1):
    for temp2 in weekly:
        if temp2 < 0:
            print("Week", week_index, "the freezing temperature below 0°C = ", temp2)


# Question 4

print("")
print("")
print("Exercise 4")
print("")

print("Daily Temperature:", daily_temperatures)


def hottest_coldest_average(daily_temperatures):
    hottest = max(daily_temperatures)

    coldest = min(daily_temperatures)

    average = sum(daily_temperatures) / len(daily_temperatures)

    print("Hottest Temperature:", hottest)
    print("Coldest Temperature:", coldest)
    print("Average Temperature:", average)

    return hottest, coldest, average


hottest, coldest, average = hottest_coldest_average(daily_temperatures)

print("Hottest Temperature:", hottest)
print("Coldest Temperature:", coldest)
print("Average Temperature:", average)


print("Daily Rainfall:", daily_rainfall)


def worst_day_record(daily_temperatures, daily_rainfall):
    worst_day = max(daily_rainfall)

    worst_day_weather_conditions = min(daily_temperatures)

    print("The worst rainfall is", worst_day, "mm")
    print("Its the worst day weather conditions ", worst_day_weather_conditions)

    return worst_day, worst_day_weather_conditions


worst_day, worst_day_weather_conditions = worst_day_record(
    daily_temperatures, daily_rainfall)

print("The worst rainfall is", worst_day, "mm")
print("Its the worst day weather conditions ", worst_day_weather_conditions)


# Question 5

print("")
print("")
print("Exercise 5")
print("")

daily_temp_ireland = [random.randint(0, 35) for _ in range(30)]
daily_rain_ireland = [random.randint(0, 10) for _ in range(30)]

daily_temp_france = [random.randint(0, 35) for _ in range(30)]
daily_rain_france = [random.randint(0, 10) for _ in range(30)]

daily_temp_spain = [random.randint(0, 35) for _ in range(30)]
daily_rain_spain = [random.randint(0, 10) for _ in range(30)]


international_weather = {
    "Ireland": {"Temperatures": daily_temp_ireland, "Rainfall": daily_rain_ireland},
    "France": {"Temperatures": daily_temp_france, "Rainfall": daily_rain_france},
    "Spain": {"Temperatures": daily_temp_spain, "Rainfall": daily_rain_spain},
}

for country, data in international_weather.items():
    print(country)
    print("Temperatures:", data["Temperatures"])
    print("Rainfall:", data["Rainfall"])
    print()


# Question 6

print("")
print("")
print("Exercise 6")
print("")

while True:
    print("")
    country_name = input(
        "Please, enter a country name. Type Ireland, France, Spain or Done to quit the program: ")

    if country_name == "Ireland":
        temperature = international_weather[country_name]["Temperatures"]
        rainfall = international_weather[country_name]["Rainfall"]
        print("Ireland Weather information:")
        hottest_coldest_average(temperature)
        worst_day_record(temperature, rainfall)

    elif country_name == "France":
        temperature = international_weather[country_name]["Temperatures"]
        rainfall = international_weather[country_name]["Rainfall"]
        print("France Weather information:")
        hottest_coldest_average(temperature)
        worst_day_record(temperature, rainfall)

    elif country_name == "Spain":
        temperature = international_weather[country_name]["Temperatures"]
        rainfall = international_weather[country_name]["Rainfall"]
        print("Spain Weather information:")
        hottest_coldest_average(temperature)
        worst_day_record(temperature, rainfall)

    elif country_name == "Done":
        print("Bye bye")
        break

    else:
        print("")
        print("You typed", country_name,
              "this is not an option. Please, choose between Ireland, France, Spain or Done.")
