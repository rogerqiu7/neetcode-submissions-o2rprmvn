class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (r > l) {
            int current_area = min(heights[r], heights[l]) * (r-l);
            max_area = max(max_area, current_area);
            if (heights[r] > heights[l]) {
                l++;
            } else {
                r--;
            }
        }
        return max_area;
    }
};
