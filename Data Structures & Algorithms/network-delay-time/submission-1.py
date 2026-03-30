class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1, n+1)}
        for node,neighbor,weight in times:
            adj_list[node].append((neighbor, weight))

        visited = set()
        answer_time = 0
        min_heap = [(0,k)]

        while min_heap:
            time, node   = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            answer_time = max(answer_time, time)

            for neighbor, weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time+weight, neighbor))

        return answer_time if len(visited) == n else -1