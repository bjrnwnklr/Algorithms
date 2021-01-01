# Shunting-yard algorithm

In computer science, the [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) is a method for parsing mathematical expressions specified in infix notation. It can produce either a postfix notation string, also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST). The algorithm was invented by Edsger Dijkstra and named the "shunting yard" algorithm because its operation resembles that of a railroad shunting yard.

The algorithm requires a definition of [operator precedence](https://en.wikipedia.org/wiki/Order_of_operations) and associativeness.

## Pseudocode algorithm 

From Wikipedia:

```
/* This implementation does not implement composite functions,functions with variable number of arguments, and unary operators. */

while there are tokens to be read:
    read a token.
    if the token is a number, then:
        push it to the output queue.
    else if the token is a function then:
        push it onto the operator stack 
    else if the token is an operator then:
        while ((there is an operator at the top of the operator stack)
              and ((the operator at the top of the operator stack has greater precedence)
                  or (the operator at the top of the operator stack has equal precedence and the token is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis)):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.
    else if the token is a left parenthesis (i.e. "("), then:
        push it onto the operator stack.
    else if the token is a right parenthesis (i.e. ")"), then:
        while the operator at the top of the operator stack is not a left parenthesis:
            pop the operator from the operator stack onto the output queue.
        /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
        if there is a left parenthesis at the top of the operator stack, then:
            pop the operator from the operator stack and discard it
        if there is a function token at the top of the operator stack, then:
            pop the function from the operator stack onto the output queue.
/* After while loop, if operator stack not null, pop everything to output queue */
if there are no more tokens to read then:
    while there are still operator tokens on the stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
exit.
```

## Python implementation

Used in AoC 2020, day 18. There is a good discussion of the various algorithms that can be used to evaluate expressions [on Reddit](https://www.reddit.com/r/adventofcode/comments/kfor25/2020_day_18_how_many_different_approaches_can_you/).

Input required is a list of terms that represent a mathematical expression in infix notation, e.g. `['1', '+', '2', '*' 3]` to represent `1 + 2 * 3`. This can be easily parsed from a string using the following code, which will read in multiple expressions separated by line breaks. The code first removes all blanks, then splits the resulting string into separate letters.

Note: this example code:
- does only consider '+' and '*' as operators, but could easily be extended to use additional operators
- each operator has to only use two arguments
- each operator has to be left associative

```python
import re 

with open(f_name, 'r') as f:
    expressions = [list(re.sub(r'\s', '', l.strip('\n'))) for l in f.readlines()]
```

This function produces RPN represented as a list of tokens. The operator precedence can be set in a dictionary, with higher values representing operators that should be considered first.

```python
op_precedence = {
    '+': 2,
    '*': 1,
    '(': 3,
    ')': 3
}

def shunting_yard(expression):
    # we need two lists:
    # - a queue that represents the final output
    # - a stack that is used to park the operators
    output_queue = []
    operator_stack = []
    # walk token by token through the input expression until we reach the end
    while expression:
        # get the first term
        term = expression.pop(0)
        # if it is a number, we add it to the output queue
        if term.isnumeric():
            output_queue.append(int(term))
        # if it is an operator, we have to decide based on op precedence what to do:
        # - if there are other operators on the operator stack, and the one on top has higher precendence,
        #   and is not an opening parenthesis, we add the top of the stack to the output queue 
        #   i.e. any operators with higher precedence get processed first
        # - only once there are no further operators on the stack, or the one on top has a lower precedence,
        #   we then add the operator to the stack (where it is on top of the next one, which has lower precedence)
        elif term in ['*', '+']:
            while (operator_stack
                   and op_precedence[operator_stack[-1]] >= op_precedence[term]
                   and operator_stack[-1] != '('
            ):
                output_queue.append(operator_stack.pop())
            operator_stack.append(term)
        # if it is an opening parenthesis, we add it to the operator stack - only temporary, as we discard
        # it once we find the closing parenthesis
        elif term == '(':
            operator_stack.append(term)
        # if it is a closing parenthesis, we next process all operators on the stack and add them to the 
        # output queue until we find the respective opening parenthesis, which we then discard
        elif term == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack[-1] == '(':
                operator_stack.pop()

    # once we are done with the expression, we empty the operator stack and add it to the output queue
    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue
```

## Reverse Polish Notation (RPN)

[Reverse Polish notation (RPN)](https://en.wikipedia.org/wiki/Reverse_Polish_notation), also known as Polish postfix notation or simply postfix notation, is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands.

This code evaluates an expression in RPN by going through each term and using a stack to store arguments for the operators, then popping off the last two once an operator is found, and pushing the result onto the stack.

Note: this implementation only recognizes `'*'` and `'+'` as valid operators, but can be easily extended. It then uses Python's `eval()` function to evaluate the expression and store the results on the stack.

```python
def eval_rpn(e):
    stack = []
    while e:
        term = e.pop(0)
        if term in ['*', '+']:
            # operator, so take the last two arguments off of the stack, evaluate the expression
            # and push the result to the stack
            stack.append(eval(str.format('{}{}{}', stack.pop(), term, stack.pop())))
        else:
            stack.append(term)
    return stack[-1]
```
