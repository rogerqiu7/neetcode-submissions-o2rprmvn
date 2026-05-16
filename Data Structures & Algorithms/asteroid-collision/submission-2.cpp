class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> myStack;

        for (int asteroid : asteroids) {
            bool alive = true;

            while (alive and !myStack.empty() and myStack.back() > 0 and asteroid < 0) {
                if (myStack.back() > -asteroid) {
                    alive = false;
                } else if (myStack.back() < -asteroid) {
                    myStack.pop_back();
                } else {
                    myStack.pop_back();
                    alive = false;
                }
            }

            if (alive) {
                myStack.push_back(asteroid);
            }
        }
        return myStack;
    }
};