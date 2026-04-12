class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> valid = {
            {'}','{'},
            {')','('},
            {']','['}
        };

        stack<char> p_stack;

        for (char c:s) {
            if (c == '}' || c == ']' || c == ')') {
                if (p_stack.empty() || p_stack.top() != valid[c]) {
                    return false;
                } 

                p_stack.pop();
            }

            else if (c == '{' || c == '[' || c == '(') {
                p_stack.push(c);
            }
        }

        if (p_stack.empty()) {
            return true;
        } else {
            return false;
        }
    }
};
