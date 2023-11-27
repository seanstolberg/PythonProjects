class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def buildExpressionTree(s):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 0

    def isOperator(ch):
        return ch in {'+', '-', '*', '/'}

    def buildTree(tokens):
        stack = []
        operator_stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(Node(int(token)))
            elif isOperator(token):
                while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
                    operator = operator_stack.pop()
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(Node(operator, left, right))
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    operator = operator_stack.pop()
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(Node(operator, left, right))
                operator_stack.pop()

        while operator_stack:
            operator = operator_stack.pop()
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(operator, left, right))

        return stack[0]

    tokens = []
    current_token = ''

    for char in s:
        if char.isdigit():
            current_token += char
        elif isOperator(char):
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char in {'(', ')'}:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)

    if current_token:
        tokens.append(current_token)

    root = buildTree(tokens)
    return inorderTraversal(root)

def inorderTraversal(root):
    result = []

    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

    dfs(root)
    return result



# Example usage:
# Example 1
s1 = "3*4-2*5"
result1 = buildExpressionTree(s1)
print(result1)
# Output: [-,*,*,3,4,2,5]

# Example 2
s2 = "2-3/(5*2)+1"
result2 = buildExpressionTree(s2)
print(result2)
# Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]

# Example 3
s3 = "1+2+3+4+5"
result3 = buildExpressionTree(s3)
print(result3)
# Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]