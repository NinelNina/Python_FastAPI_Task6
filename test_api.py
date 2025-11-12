import requests


BASE_URL = "http://localhost:8000"


def test_api():
    print("=== Тестирование калькулятора API ===\n")

    # 1. Очистка калькулятора
    print("1. Очистка калькулятора:")
    response = requests.delete(f"{BASE_URL}/expression/clear")
    print(f"Status: {response.status_code}, Response: {response.json()}\n")

    # 2. Добавление простого выражения
    print("2. Добавление простого выражения 10 + 5:")
    response = requests.post(
        f"{BASE_URL}/expression/simple",
        json={"a": 10, "op": "+", "b": 5}
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Результат: {result['result']}")
        print(f"Выражение: {result['expression']}\n")

    # 3. Добавление еще одной операции
    print("3. Добавление операции * 2:")
    response = requests.post(
        f"{BASE_URL}/expression/simple",
        json={"a": 15, "op": "*", "b": 2}
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Результат: {result['result']}")
        print(f"Выражение: {result['expression']}\n")

    # 4. Просмотр текущего состояния
    print("4. Текущее состояние:")
    response = requests.get(f"{BASE_URL}/expression")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        state = response.json()
        print(f"Выражение: {state['expression']}")
        print(f"Текущее значение: {state['current_value']}")
        print(f"Шаги вычисления: {state['steps']}\n")

    # 5. Прямое вычисление сложного выражения
    print("5. Прямое вычисление (10+5)*2:")
    response = requests.post(
        f"{BASE_URL}/calculate/direct",
        json={"expression": "(10+5)*2"}
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Результат: {result['result']}")
        print(f"Шаги: {result['steps']}\n")

    # 6. Установка сложного выражения
    print("6. Установка сложного выражения:")
    response = requests.post(
        f"{BASE_URL}/expression/complex",
        json={"expression": "(20+10)/3 + 5*2"}
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Результат: {result['result']}")
        print(f"Выражение: {result['expression']}\n")


if __name__ == "__main__":
    test_api()
