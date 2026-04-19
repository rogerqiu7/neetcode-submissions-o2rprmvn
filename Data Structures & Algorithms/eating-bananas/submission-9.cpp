class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        int result = 0;

        while (l <= r) {
            int mid = (l+r) / 2;

            long long totalTime = 0;

            for (int pile:piles) {
                int currentTime = (pile+mid-1) / mid;
                totalTime += currentTime;
            }

            if (totalTime <= h) {
                result = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }

        }   

        return result;
    }
};
