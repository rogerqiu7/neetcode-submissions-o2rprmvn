class MinStack {
public:
    stack<int> _stack;

    MinStack() {
    }
    
    void push(int val) {
        _stack.push(val);
    }
    
    void pop() {
        _stack.pop();
    }
    
    int top() {
        return _stack.top();
    }
    
    int getMin() {
        stack<int> temp = _stack;
        int minVal = temp.top();

        while(!temp.empty()) {
            int num = temp.top();
            if (num < minVal) {
                minVal = num;
            }
            temp.pop();
        }
        return minVal;
    }
};
