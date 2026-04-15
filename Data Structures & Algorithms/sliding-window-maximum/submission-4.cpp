class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;

        int l = 0;
        int r = k;

        while (r <= nums.size()) {
            vector<int> subArray(nums.begin() + l, nums.begin() + r);
            int maxVal = *max_element(subArray.begin(), subArray.end());
            res.push_back(maxVal);
            l++;
            r++;
        }

        return res;
    }
};
