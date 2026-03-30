class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for source, dest in tickets:
            adj_list[source].append(dest)

        res = []

        for source in adj_list:
            adj_list[source].sort(reverse=True)

        def dfs(source):
            while adj_list[source]:
                neighbor = adj_list[source].pop()
                dfs(neighbor)
            res.append(source)

        dfs("JFK")

        return res[::-1]