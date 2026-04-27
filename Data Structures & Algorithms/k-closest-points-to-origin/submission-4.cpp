class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> distances;
        for (int i = 0; i < points.size(); i++) {
            int x = points[i][0];
            int y = points[i][1];

            int distance = x*x + y*y;
            distances.push_back({distance, x, y});
        }

        sort(distances.begin(), distances.end());

        vector<vector<int>> res;

        for (int i = 0; i < k; i++) {
            res.push_back({distances[i][1], distances[i][2]});
        }

        return res;
    }
};
