from enum import Enum
from typing import List

from pydantic import BaseModel


class Operation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


class SimpleExpression(BaseModel):
    a: float
    op: Operation
    b: float


class ComplexExpression(BaseModel):
    expression: str


class ExpressionState(BaseModel):
    expression: str
    steps: List[str]
    current_value: float


class CalculationResult(BaseModel):
    expression: str
    result: float
    steps: List[str]
