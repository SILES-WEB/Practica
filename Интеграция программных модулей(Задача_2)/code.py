def find_min_max_passengers(routes):
    min_passengers = [float('inf')] * len(routes)
    max_passengers = [float('-inf')] * len(routes)

    for city in range(len(routes)):
        for route in range(len(routes[city])):
            passengers = routes[city][route]
            if passengers < min_passengers[city]:
                min_passengers[city] = passengers
            if passengers > max_passengers[city]:
                max_passengers[city] = passengers

    return min_passengers, max_passengers

# Пример входных данных (количество пассажиров для каждого маршрута в каждом городе)
routes = [
    [10, 20, 15],  # Город 1
    [25, 18, 30],  # Город 2
    [12, 22, 17]   # Город 3
]

min_passengers, max_passengers = find_min_max_passengers(routes)

for city in range(len(routes)):
    min_route = min_passengers[city]
    max_route = max_passengers[city]
    print(f"Для города {city + 1}: Минимальное количество пассажиров - {min_route}, Максимальное количество пассажиров - {max_route}")
