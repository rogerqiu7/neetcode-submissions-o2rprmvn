class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int missing = 1;
        while (true) {
            bool flag = true;
            for (int i = 0; i <nums.size(); i++) {
                if (nums[i] == missing) {
                    flag = false;
                    break;
                }
            }

            if (flag == true) {
                return missing;
            }
            missing++;
        }
    }
};