class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        
        for (int i=0;i<s.size();i++){
            set<int> seen;
            int current = 0;

            for (int j = i;j<s.size();j++) {
                if (seen.count(s[j]) == 0) {
                    seen.insert(s[j]);
                    current++;
                    res = max(res,current);
                } else {
                    break;
                }
            }
        }
        return res;
    }
};
