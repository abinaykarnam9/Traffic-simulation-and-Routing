import networkx as nx
import random

# Create a random graph with 100 nodes and average connectivity of 3
G = nx.random_regular_graph(3, 100)

# Initialize service queues for vehicles
fleet = [[] for _ in range(60)]

# Define a function to find the shortest path given the current positions of vehicles
def find_shortest_path(vehicle_id, current_position):
    target = random.choice(list(G.nodes()))
    while target == current_position:
        target = random.choice(list(G.nodes()))
    path = nx.shortest_path(G, source=current_position, target=target)
    return path

# Simulate for one day (24 hours)
total_distance = 0
total_trips = 0
hours_per_day = 24

for hour in range(hours_per_day):
    # Generate a random number of reservations per hour (450 to 600)
    reservations = random.randint(450, 600)
    
    for _ in range(reservations):
        vehicle_id = random.randint(0, 59)
        current_position = fleet[vehicle_id][-1] if fleet[vehicle_id] else random.choice(list(G.nodes()))
        path = find_shortest_path(vehicle_id, current_position)
        fleet[vehicle_id] += path
        total_distance += len(path) - 1  # Distance is the number of edges traversed
        total_trips += 1

# Calculate average distance traveled per day
average_distance_per_day = total_distance / hours_per_day

# Calculate average number of trips per day
average_trips_per_day = total_trips / hours_per_day

# Print results
print(f"Average Distance Traveled per Day: {average_distance_per_day:.2f} edges")
print(f"Average Number of Trips per Day: {average_trips_per_day:.2f} trips")
