#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_numeric(value):
    """Check if the input value is numeric."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def calculate(num1, num2, operation):
    """Perform the specified arithmetic operation on two numbers."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

def main():
    """Main function to run the calculator application."""
    print("電卓アプリケーション (Calculator Application)")
    print("四則演算 (+, -, *, /) を行います。")
    
    # Get first number input
    value1 = input("1つ目の数値を入力してください: ")
    if not is_numeric(value1):
        print("🙅")
        return
    
    # Get second number input
    value2 = input("2つ目の数値を入力してください: ")
    if not is_numeric(value2):
        print("🙅")
        return
    
    # Convert inputs to float
    num1 = float(value1)
    num2 = float(value2)
    
    # Get operation
    operation = input("演算子 (+, -, *, /) を入力してください: ")
    if operation not in ['+', '-', '*', '/']:
        print("🙅")
        return
    
    # Perform calculation
    result = calculate(num1, num2, operation)
    
    # Display result
    print(f"結果: {result}")

if __name__ == "__main__":
    main()