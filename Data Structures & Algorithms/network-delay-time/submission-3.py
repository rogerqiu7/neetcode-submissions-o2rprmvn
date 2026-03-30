class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1, n+1)}
        for source,target,distance in times:
            adj_list[source].append((target,distance))

        total_signal_time = 0
        visited = set()
        min_heap = [(0,k)]

        while min_heap:
            current_time,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_signal_time = max(total_signal_time, current_time)

            for neighbor,distance in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (distance+current_time, neighbor))

        return total_signal_time if len(visited) == n else -1