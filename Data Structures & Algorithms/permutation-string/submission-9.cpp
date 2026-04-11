class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        string sorted_s1 = s1;
        sort(sorted_s1.begin(), sorted_s1.end());

        int k = s1.size();

        for (int i=0; i + k <= s2.size(); i++) {
            string subStr = s2.substr(i,k);
            sort(subStr.begin(), subStr.end());

                if (sorted_s1 == subStr) {
                    return true;
                }
            }

        return false;
    }
};
