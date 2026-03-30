class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for source, destination in tickets:
            adj_list[source].append(destination)

        for source in adj_list:
            adj_list[source].sort(reverse=True)

        res = []
        def dfs(src):
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]