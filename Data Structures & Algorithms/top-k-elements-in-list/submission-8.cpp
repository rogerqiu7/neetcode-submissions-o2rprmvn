class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> num_freq;
        for (int num:nums) {
            num_freq[num] += 1;
        }

        vector<pair<int,int>> freq_num;
        for (auto& [num,freq] : num_freq) {
            freq_num.push_back({freq,num});
        }

        sort(freq_num.rbegin(),freq_num.rend());

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(freq_num[i].second);
        }

        return res;
    }
};
