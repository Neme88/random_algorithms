# Greedy Algorithm: Dijkstra's Algorithm for Shortest Path
import heapq
def dijkstra(graph, start):
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
print(f"Shortest paths from A: {dijkstra(graph, 'A')}")
