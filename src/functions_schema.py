math_exp_evaluator={"name": "evaluate_expression",
                    "description": "Performs calculation on the given mathematical expression",
                    "parameters":{
                        "type": "object",
                        "properties": {
                        "expression":{
                            "type": "string",
                            "description": "Mathematical expression to be evaluated. Ex: 1 + 2 * (3/2) - 6"
                            }
                        },
                        "required": ["expression"]
                    }
                    }
