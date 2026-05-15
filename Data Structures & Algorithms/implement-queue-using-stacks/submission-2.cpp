class MyQueue {
public:

    queue<int> myQueue;

    MyQueue() {
        
    }
    
    void push(int x) {
        myQueue.push(x);
    }
    
    int pop() {
        int x = myQueue.front();
        myQueue.pop();
        return x;
    }
    
    int peek() {
        return myQueue.front();
    }
    
    bool empty() {
        if (myQueue.empty()) {
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */