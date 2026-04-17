class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;

        for (int i = 0; i < heights.size();i++) {
            int height = heights[i];

            int width = 1;

            int r = i + 1;
            while (r <heights.size() and heights[r] >= height) {
                width++;
                r++;
            }

            int l = i - 1;
            while (l >= 0 and heights[l] >= height) {
                width++;
                l--;
            }

            int currentArea = height * width;
            maxArea = max(maxArea, currentArea);
        }

        return maxArea;
    }
};
