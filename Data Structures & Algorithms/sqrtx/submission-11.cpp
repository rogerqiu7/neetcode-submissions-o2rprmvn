class Solution {
public:
    int mySqrt(int x) {
        int res = 0;

        for (long long i = 0; i <= x; i++) {
            if (i*i <= x) {
                res = i;
            } else {
                break;
            }
        }

        return res;
    }
};