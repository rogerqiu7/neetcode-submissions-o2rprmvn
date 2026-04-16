class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        int l = 0;

        while (l+k <= nums.size()) {
            vector<int> sub_array(nums.begin() + l, nums.begin() + (l+k));
            int maxVal = *max_element(sub_array.begin(), sub_array.end());
            res.push_back(maxVal);
            l++;
        }

        return res;
    }
};
