import numexpr
import json

def evaluate_expression(expression):
    try:
        value = numexpr.evaluate(expression.strip())
    except Exception as e:
        value = f"This is an unsupported mathematical expression"
    return value

def execute_function_call(message):
    if message["function_call"]["name"] == "evaluate_expression":
        expression = json.loads(message["function_call"]["arguments"])["expression"]
        out = evaluate_expression(expression)
        results = out if isinstance(out, str) else f"{float(out)}"
    else:
        results = f"Error: function {message['function_call']['name']} does not exist"
    return results
