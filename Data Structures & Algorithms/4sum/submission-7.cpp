class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        set<vector<int>> res;
        sort(nums.begin(),nums.end());
        
        int n = nums.size();

        for (int i = 0; i <n;i++) {
            for (int j = i+1; j < n;j++) {
                for (int k = j+1; k < n; k++) {
                    for (int l = k+1; l<n; l++) {
                        if ((long long) nums[i] + nums[j] + nums[k] + nums[l] == target) {
                            res.insert({nums[i],nums[j],nums[k],nums[l]});
                        }
                    }
                }
            }
        }

        return vector<vector<int>>(res.begin(), res.end());
    }
};