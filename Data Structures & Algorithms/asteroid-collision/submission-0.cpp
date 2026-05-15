class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (int asteroid : asteroids) {
            bool alive = true;

            // Collision only happens when stack top moves right
            // and current asteroid moves left.
            while (alive && !stack.empty() && stack.back() > 0 && asteroid < 0) {
                int top = stack.back();

                if (top < -asteroid) {
                    // Top asteroid is smaller, so it explodes.
                    stack.pop_back();
                } 
                else if (top == -asteroid) {
                    // Same size, so both explode.
                    stack.pop_back();
                    alive = false;
                } 
                else {
                    // Current asteroid is smaller, so it explodes.
                    alive = false;
                }
            }
            if (alive) {
                stack.push_back(asteroid);
            }
        }
        return stack;
    }
};