class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1, n+1)}
        for source, target, distance in times:
            adj_list[source].append((distance, target))

        visited = set()
        total_signal_time = 0
        min_heap = [(0,k)]

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            if current_node in visited:
                continue
            visited.add(current_node)
            total_signal_time = max(total_signal_time, current_distance)

            for neighbor_distance, neighbor in adj_list[current_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_distance+current_distance, neighbor))

        return total_signal_time if len(visited) == n else -1
