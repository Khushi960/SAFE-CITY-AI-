import heapq

# --- Pune City Graph ---
# Nodes = real Pune locations
# Edges = (destination, distance_km)
PUNE_GRAPH = {
    "Shivajinagar":     [("Deccan",       2.1), ("FC Road",       1.8), ("Kothrud",       5.2)],
    "Deccan":           [("Shivajinagar", 2.1), ("Swargate",      3.5), ("Karve Nagar",   3.8)],
    "FC Road":          [("Shivajinagar", 1.8), ("Baner",         6.0), ("Aundh",         5.5)],
    "Swargate":         [("Deccan",       3.5), ("Hadapsar",      7.2), ("Katraj",        5.0), ("Market Yard",   2.0)],
    "Hadapsar":         [("Swargate",     7.2), ("Magarpatta",    2.5), ("Kondhwa",       5.0)],
    "Koregaon Park":    [("Viman Nagar",  4.5), ("Kalyani Nagar", 2.0), ("Magarpatta",    6.0)],
    "Viman Nagar":      [("Koregaon Park",4.5), ("Kalyani Nagar", 3.0), ("Kharadi",       3.5)],
    "Kharadi":          [("Viman Nagar",  3.5), ("Wagholi",       5.0), ("Magarpatta",    4.5)],
    "Baner":            [("FC Road",      6.0), ("Aundh",         2.5), ("Balewadi",      3.0), ("Hinjewadi",     7.0)],
    "Aundh":            [("FC Road",      5.5), ("Baner",         2.5), ("Wakad",         5.0), ("Pimple Saudagar",4.0)],
    "Kothrud":          [("Shivajinagar", 5.2), ("Karve Nagar",   2.0), ("Warje",         4.0)],
    "Karve Nagar":      [("Deccan",       3.8), ("Kothrud",       2.0), ("Katraj",        6.0)],
    "Warje":            [("Kothrud",      4.0), ("Katraj",        5.5)],
    "Katraj":           [("Swargate",     5.0), ("Karve Nagar",   6.0), ("Warje",         5.5), ("Kondhwa",       4.0)],
    "Kondhwa":          [("Katraj",       4.0), ("Hadapsar",      5.0), ("Undri",         3.5)],
    "Undri":            [("Kondhwa",      3.5)],
    "Magarpatta":       [("Hadapsar",     2.5), ("Kharadi",       4.5), ("Koregaon Park", 6.0)],
    "Kalyani Nagar":    [("Koregaon Park",2.0), ("Viman Nagar",   3.0), ("Kharadi",       4.0)],
    "Wagholi":          [("Kharadi",      5.0)],
    "Hinjewadi":        [("Baner",        7.0), ("Wakad",         3.5), ("Pimple Saudagar",5.0)],
    "Wakad":            [("Aundh",        5.0), ("Hinjewadi",     3.5), ("Pimple Saudagar",3.0)],
    "Pimple Saudagar":  [("Aundh",        4.0), ("Wakad",         3.0), ("Hinjewadi",     5.0)],
    "Balewadi":         [("Baner",        3.0), ("Wakad",         4.0)],
    "Market Yard":      [("Swargate",     2.0), ("Karve Nagar",   3.5)],
}

# Approximate lat/lon for heuristic (straight-line distance proxy)
NODE_COORDS = {
    "Shivajinagar":    (18.5308, 73.8474),
    "Deccan":          (18.5162, 73.8400),
    "FC Road":         (18.5270, 73.8401),
    "Swargate":        (18.5018, 73.8560),
    "Hadapsar":        (18.5018, 73.9285),
    "Koregaon Park":   (18.5362, 73.8939),
    "Viman Nagar":     (18.5679, 73.9143),
    "Kharadi":         (18.5515, 73.9461),
    "Baner":           (18.5590, 73.7868),
    "Aundh":           (18.5584, 73.8079),
    "Kothrud":         (18.5074, 73.8088),
    "Karve Nagar":     (18.4955, 73.8230),
    "Warje":           (18.4813, 73.8050),
    "Katraj":          (18.4528, 73.8563),
    "Kondhwa":         (18.4632, 73.8890),
    "Undri":           (18.4451, 73.9078),
    "Magarpatta":      (18.5112, 73.9275),
    "Kalyani Nagar":   (18.5440, 73.9008),
    "Wagholi":         (18.5786, 73.9808),
    "Hinjewadi":       (18.5906, 73.7381),
    "Wakad":           (18.5967, 73.7614),
    "Pimple Saudagar": (18.6103, 73.7898),
    "Balewadi":        (18.5798, 73.7812),
    "Market Yard":     (18.4976, 73.8475),
}

def haversine(n1, n2):
    """Straight-line km between two nodes (used as A* heuristic)."""
    import math
    if n1 not in NODE_COORDS or n2 not in NODE_COORDS:
        return 1
    lat1, lon1 = NODE_COORDS[n1]
    lat2, lon2 = NODE_COORDS[n2]
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def astar(graph, start, goal):
    """A* pathfinding. Returns (path, total_cost) or (None, None)."""
    if start not in graph or goal not in graph:
        return None, None

    open_list = []
    heapq.heappush(open_list, (0, start))
    g = {node: float('inf') for node in graph}
    g[start] = 0
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, round(g[goal], 2)

        for neighbor, cost in graph.get(current, []):
            new_cost = g[current] + cost
            if new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + haversine(neighbor, goal)
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None, None


if __name__ == "__main__":
    path, cost = astar(PUNE_GRAPH, "Shivajinagar", "Hinjewadi")
    print("Path:", " → ".join(path))
    print("Distance:", cost, "km")
