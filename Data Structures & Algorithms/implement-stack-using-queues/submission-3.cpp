class MyStack {
public:

    stack<int> myStack;

    MyStack() {
        
    }
    
    void push(int x) {
        myStack.push(x);
    }
    
    int pop() {
        int x = myStack.top();
        myStack.pop();
        return x;
    }
    
    int top() {
        return myStack.top();
    }
    
    bool empty() {
        if (myStack.empty()) {
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */