import json
from src.functions_schema import math_exp_evaluator
from src.utilities import (
    chat_completion_request, 
    pretty_print_conversation, 
    append_assistant_messages,
    get_result)
from src.system_prompt import system_instruction
import chainlit as cl


chat_messages = [
    {"role": "system", "content":system_instruction}
]
functions = [math_exp_evaluator]

@cl.on_chat_start
async def start_chat():
    await cl.Message(content ="Let's crunch some numbers!!!!").send()


@cl.on_message
async def eval_exp(msg:str):
    global chat_messages
    chat_messages.append({"role":"user", "content":msg})
    print(chat_messages)
    chat_response = chat_completion_request(
    chat_messages, functions=functions, function_call="auto"
    )
    # takes current messages list and chat response
    print(chat_response.json())
    chat_messages = append_assistant_messages(chat_messages, chat_response)
    result = get_result(chat_messages)
    await cl.Message(
        content=result
        ).send()




