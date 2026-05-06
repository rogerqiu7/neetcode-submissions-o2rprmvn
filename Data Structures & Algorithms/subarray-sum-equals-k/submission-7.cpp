class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0;
        for (int i = 0; i<nums.size();i++) {
            int current = 0;
            for (int j = i; j<nums.size(); j++) {
                current += nums[j];
                if (current == k) {
                    res++;
                }
            }
        }
        return res;
    }
};