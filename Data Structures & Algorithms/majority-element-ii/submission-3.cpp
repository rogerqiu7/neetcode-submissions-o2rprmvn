class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res;
        int totalCount = nums.size();
        unordered_map<int,int> counter;

        for (int num : nums) {
            counter[num] += 1;
        }

        for (auto [num,freq] : counter ) {
            double percentage = (double)freq / totalCount;
            if (percentage > 1.0 / 3.0) {
                res.push_back(num);
            }
        }

        return res;
    }
};