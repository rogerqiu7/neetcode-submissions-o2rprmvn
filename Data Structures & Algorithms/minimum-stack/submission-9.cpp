class MinStack {
public:
    MinStack() {
        
    }

    stack<int> minStack;
    
    void push(int val) {
        minStack.push(val);
    }
    
    void pop() {
        minStack.pop();
    }
    
    int top() {
        return minStack.top();
    }
    
    int getMin() {
        stack<int> temp = minStack;
        int min = temp.top();

        while (!temp.empty()) {
            int value = temp.top();
            if (value < min) {
                min = value;
            }
            temp.pop();
        }

        return min;
    }
};
