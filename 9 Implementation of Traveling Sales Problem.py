import numpy as np

def nearest_neighbor(distances):
    num_cities = distances.shape[0]
    current_city = 0  # Start at city 0 arbitrarily
    visited = {current_city}
    route = [current_city]
    cost = 0

    while len(visited) < num_cities:
        unvisited = np.where(~np.isin(np.arange(num_cities), list(visited)))[0]
        next_index = np.argmin(distances[current_city][unvisited])
        next_city = unvisited[next_index]  # Correctly identify the next city

        route.append(next_city)
        cost += distances[current_city, next_city]

        current_city = next_city  # Update the current city to the next city
        visited.add(current_city)

    # Return to the starting city to complete the tour
    route.append(route[0])
    cost += distances[current_city, route[0]]

    return route, cost

# Example usage
distance_matrix = np.array([
    [0, 20, 30, 15, 10],
    [20, 0, 12, 32, 25],
    [30, 12, 0, 18, 40],
    [15, 32, 18, 0, 22],
    [10, 25, 40, 22, 0]
])

route, cost = nearest_neighbor(distance_matrix)
print("Route:", route)
print("Total cost:", cost)
