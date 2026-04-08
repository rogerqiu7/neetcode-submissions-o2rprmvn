class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int max_area = 0;

        while (r>l) {
            int current = min(heights[r],heights[l]) * (r-l);
            max_area = max(max_area,current);
            if (heights[r] > heights[l]) {
                l++;
            } else {
                r--;
            }
        }

        return max_area;
    }
};
