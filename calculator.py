from parser import ExpressionParser


class CalculatorEngine:
    def __init__(self):
        self.parser = ExpressionParser()
        self.current_expression = ""
        self.steps = []
        self.current_value = None

    def set_expression(self, expression: str):
        self.current_expression = expression
        self._evaluate_expression()

    def add_simple_operation(self, a: float, op: str, b: float):
        if self.current_expression:
            self.current_expression += f" {op} ({a} {op} {b})"
        else:
            self.current_expression = f"({a} {op} {b})"

        self._evaluate_expression()

    def _evaluate_expression(self):
        if not self.current_expression:
            self.current_value = None
            self.steps = []
            return

        try:
            rpn = self.parser.parse_expression(self.current_expression)
            self.current_value, self.steps = self.parser.evaluate_rpn(rpn)
        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {e}")

    def get_state(self) -> dict:
        return {
            "expression": self.current_expression,
            "steps": self.steps,
            "current_value": self.current_value
        }

    def clear(self):
        self.current_expression = ""
        self.steps = []
        self.current_value = None
