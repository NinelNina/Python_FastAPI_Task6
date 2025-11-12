from fastapi import FastAPI, HTTPException
from models import (
    SimpleExpression, ComplexExpression, ExpressionState,
    CalculationResult
)
from calculator import CalculatorEngine
import uvicorn

app = FastAPI(
    title="Калькулятор"
)

calculator = CalculatorEngine()


@app.post("/expression/simple", response_model=CalculationResult)
async def add_simple_expression(expr: SimpleExpression):
    try:
        calculator.add_simple_operation(expr.a, expr.op.value, expr.b)
        state = calculator.get_state()

        return CalculationResult(
            expression=state["expression"],
            result=state["current_value"],
            steps=state["steps"]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/expression/complex", response_model=CalculationResult)
async def set_complex_expression(expr: ComplexExpression):
    try:
        calculator.set_expression(expr.expression)
        state = calculator.get_state()

        return CalculationResult(
            expression=state["expression"],
            result=state["current_value"],
            steps=state["steps"]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/expression", response_model=ExpressionState)
async def get_current_expression():
    return ExpressionState(**calculator.get_state())


@app.post("/expression/evaluate")
async def evaluate_expression():
    state = calculator.get_state()

    if state["current_value"] is None:
        raise HTTPException(status_code=400, detail="Нет выражения для вычисления")

    return {"result": state["current_value"]}


@app.delete("/expression/clear")
async def clear_expression():
    calculator.clear()
    return {"message": "Выражение очищено"}


@app.post("/calculate/direct", response_model=CalculationResult)
async def calculate_direct(expr: ComplexExpression):
    try:
        temp_calc = CalculatorEngine()
        temp_calc.set_expression(expr.expression)
        state = temp_calc.get_state()

        return CalculationResult(
            expression=state["expression"],
            result=state["current_value"],
            steps=state["steps"]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
