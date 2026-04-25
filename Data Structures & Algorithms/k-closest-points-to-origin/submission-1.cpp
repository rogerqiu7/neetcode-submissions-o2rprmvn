class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        // Step 1: store [distance, x, y]
        vector<vector<int>> distPoints;

        for (int i = 0; i < points.size(); i++) {
            int x = points[i][0];
            int y = points[i][1];

            int dist = x*x + y*y;

            distPoints.push_back({dist, x, y});
        }

        // Step 2: sort (default sort works)
        sort(distPoints.begin(), distPoints.end());

        // Step 3: take first k
        vector<vector<int>> ans;

        for (int i = 0; i < k; i++) {
            ans.push_back({distPoints[i][1], distPoints[i][2]});
        }

        return ans;
    }
};