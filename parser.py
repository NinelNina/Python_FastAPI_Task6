from typing import List, Union, Tuple


class ExpressionParser:
    def __init__(self):
        self.operators_priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def parse_expression(self, expression: str) -> List[Union[float, str]]:
        expression = expression.replace(' ', '')
        output = []
        operators = []

        i = 0
        while i < len(expression):
            char = expression[i]

            if char.isdigit() or char == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num = float(expression[i:j])
                output.append(num)
                i = j
                continue

            elif char == '(':
                operators.append(char)

            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()

            elif char in self.operators_priority:
                while (operators and operators[-1] != '(' and
                       self.operators_priority.get(operators[-1], 0) >= self.operators_priority[char]):
                    output.append(operators.pop())
                operators.append(char)

            i += 1

        while operators:
            output.append(operators.pop())

        return output

    def evaluate_rpn(self, rpn: List[Union[float, str]]) -> Tuple[float, List[str]]:
        stack = []
        steps = []
        result = ''

        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Деление на ноль")
                    result = a / b

                steps.append(f"{a} {token} {b} = {result}")
                stack.append(result)

        return stack[0], steps
