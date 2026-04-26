class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> distances;
        vector<vector<int>> answer;

        for (int i = 0; i < points.size(); i++) {
            int distance = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            distances.push_back({distance, points[i][0], points[i][1]});
        }

        sort(distances.begin(), distances.end());

        for (int i = 0; i < k; i++) {
            answer.push_back({distances[i][1], distances[i][2]});
        }

        return answer;

    }
};
