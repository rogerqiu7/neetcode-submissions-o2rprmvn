class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1, n+1)}
        for node,neighbor,distance in times:
            adj_list[node].append((neighbor,distance))

        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, weight)

            for neighbor, neighbor_weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight+neighbor_weight, neighbor))

        return time if len(visited) == n else -1