class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> anagram_map;
        for (string str:strs) {
            string sorted = str;
            sort(sorted.begin(),sorted.end());
            anagram_map[sorted].push_back(str);
        }
        vector<vector<string>> res;

        for (auto& [key,value] : anagram_map) {
            res.push_back(value);
        }

        return res;
    }
};
