class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1, n+1)}
        for source,target,travel_time in times:
            adj_list[source].append((target, travel_time))

        visited = set()
        total_signal_time = 0
        min_heap = [(0,k)]

        while min_heap:
            current_signal_time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_signal_time = max(total_signal_time, current_signal_time)

            for target, travel_time in adj_list[node]:
                if target not in visited:
                    heapq.heappush(min_heap, (current_signal_time+travel_time, target))

        return total_signal_time if len(visited) == n else -1