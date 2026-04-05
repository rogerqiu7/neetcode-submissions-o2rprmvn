class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned;
        for (char c : s) {
            if (isalnum(c)) {
                cleaned+=tolower(c);
            }
        }

        string res = cleaned;

        reverse(res.begin(), res.end());

        return cleaned == res;
    }
};
