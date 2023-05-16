class Stack:
    def __init__(self):
        self.list = list()
        self.top = -1
        
    def is_empty(self):
        if self.top == -1:
            print("Stack is empty")
     
    def is_full(self):
         if len(self.list) == self.size :
             print("Stack is full")
     
    def size(self):
        print(self.size)

    def push(self, item):
        if not self.is_full():
            self.list.append(item)
            self.top+=1
        else:
            print("Stack is full")
        
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            print("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            print(self.list[-1])
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack will be : ",self.list)
            
    def printempty(self):
        print(self.list)
            

def evaluate_postfix(expr):
        stack = Stack()
        for c in expr:
        # If the character is a digit, push it onto the stack
          if c.isdigit():
            stack.push(int(c))
        # If the character is an operator, pop two operands from the stack and apply the operator
          else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if c == '+':
                result = operand1 + operand2
            elif c == '-':
                result = operand1 - operand2
            elif c == '*':
                result = operand1 * operand2
            elif c == '/':
                result = operand1 / operand2
            else:
                raise ValueError('Invalid operator: ' + c)
            # Push the result onto the stack
            stack.push(result)
    # The final result will be left on the stack
        return stack.pop()

exp = input("Enter a Postfix expression: ").split()
# Example usage
print(evaluate_postfix(exp))
