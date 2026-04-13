class Solution {
public:
    bool isValid(string s) {
        stack<char> p_stack;
        unordered_map<char,char> valid = {
            {'}','{'},
            {')','('},
            {']','['}
        };

        for (char c:s) {
            if (c == '{' || c == '[' || c == '(') {
                p_stack.push(c);
            } else if (c == '}' || c == ']' || c == ')') {
                if (p_stack.empty() || p_stack.top() != valid[c]) {
                    return false;
                }
                p_stack.pop();
            }
        }

        if (p_stack.empty()) {
            return true;
        } else {
            return false;
        }
    }
};
