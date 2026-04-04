class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int zero_count = count(nums.begin(), nums.end(), 0);
        int product = 1;
        for (int& num:nums) {
            if (num != 0) {
                product *= num;
            }
        }

        if (zero_count > 1) {
            vector<int> res(nums.size(), 0);
            return res;
        }

        if (zero_count == 1) {
            for (int& num:nums) {
                if (num != 0) {
                    res.push_back(0);
                } else {
                    res.push_back(product);
                }
            }

            return res;
        }

        for (int& num:nums) {
            int answer = product / num;
            res.push_back(answer);
            }

        return res;

    }
};
