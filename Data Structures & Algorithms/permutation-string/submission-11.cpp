class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int k = s1.size();
        sort(s1.begin(),s1.end());

        for (int i = 0; i+k <= s2.size(); i++) {
            string subStr = s2.substr(i, k);
            sort(subStr.begin(),subStr.end());

            if (s1 == subStr) {
                return true;
            }
        }

        return false;


    }
};
