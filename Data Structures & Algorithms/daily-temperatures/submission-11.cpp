class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res;

        for (int i = 0; i<temperatures.size();i++) {
            bool found = false;
            int count = 0;

            for (int j = i+1; j<temperatures.size();j++) {
                count++;

                if (temperatures[j] > temperatures[i]) {
                    found = true;
                    break;
                }
            }

            if (found==true) {
                res.push_back(count);
            } else {
                res.push_back(0);
            }
            
        }
        return res;
    }
};
