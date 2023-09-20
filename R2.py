import networkx as nx
import random

# Create a random graph with 100 nodes and an average connectivity of approximately 3
G = nx.erdos_renyi_graph(100, 0.03)

# Initialize service queues for vehicles
fleet = [[] for _ in range(30)]

# Simulate for 600 clock ticks (1 minute = 1 clock tick)
clock_ticks = 600

# Initialize customer counter
customer_counter = 0

print("Customer  Pick-upNode  DropNode  AvgDistance  AvgTime")
for tick in range(clock_ticks):
    # Generate reservations
    if random.random() < 0.3:
        customer_counter += 1
        customer = f"C{customer_counter}"
        
        # Ensure that pickup and drop-off nodes are within the valid range
        valid_nodes = list(G.nodes())
        pickup_node = random.choice(valid_nodes)
        valid_nodes.remove(pickup_node)  # Remove pickup node from valid nodes
        dropoff_node = random.choice(valid_nodes)
        
        # Check if a path exists between pickup and drop-off nodes
        if nx.has_path(G, pickup_node, dropoff_node):
            path = nx.shortest_path(G, source=pickup_node, target=dropoff_node)
            avg_distance = len(path) - 1  # Distance is the number of edges traversed
            avg_time = avg_distance  # Assume 1 unit of time per edge traversed
            print(f"{customer}          {pickup_node}          {dropoff_node}          {avg_distance}          {avg_time}")
        else:
            print(f"{customer}          {pickup_node}          {dropoff_node}          No path found")
