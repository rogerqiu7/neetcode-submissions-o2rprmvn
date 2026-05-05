class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res;
        unordered_map<int,int> counter;

        for (int num:nums) {
            counter[num] += 1;
        }

        for (auto [num,freq] : counter ) {
            if (freq > (nums.size() / 3)) {
                res.push_back(num);
            }
        }

        return res;
    }
};