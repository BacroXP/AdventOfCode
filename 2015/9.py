from itertools import permutations
import libs.input

def parse_input(input_data):
    distances = {}
    cities = set()
    
    for line in input_data:
        parts = line.split(" ")
        city1, city2, distance = parts[0], parts[2], int(parts[4])

        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance
        
        cities.add(city1)
        cities.add(city2)
    
    return distances, cities

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i + 1])]
    return total_distance

def find_route(input_data):
    distances, cities = parse_input(input_data)
    shortest_distance = float("inf")
    longest_distance = float("-1")

    for route in permutations(cities):
        total_distance = calculate_distance(route, distances)
        if total_distance < shortest_distance:
            shortest_distance = total_distance
        if total_distance > longest_distance:
            longest_distance = total_distance

    
    return shortest_distance, longest_distance

input_data = libs.input.file()

# Part 1
print(find_route(input_data)[0])

# Part 2
print(find_route(input_data)[1])
