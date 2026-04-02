class Solution {
public:
    vector<string> res;

    string encode(vector<string>& strs) {
        string combined;
        for (string str : strs) {
            res.push_back(str);
            combined += str;
        }
        return combined;
    }

    vector<string> decode(string s) {
        return res;
    }
};
