class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int max_l = height[l];
        int max_r = height[r];
        int total_area = 0;

        while (r>l) {
            if (height[r]>=height[l]) {
                l++;
                max_l = max(max_l, height[l]);
                total_area += max_l - height[l];
            } else {
                r--;
                max_r = max(max_r, height[r]);
                total_area += max_r - height[r];
            }
        }

        return total_area;
    }
};
