from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

import torch

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)

print("College Assistant Ready!")

SYSTEM_PROMPT = """
You are College Assistant AI.

Help students with:

Programming
Python
Java
DBMS
Operating Systems
Machine Learning
Deep Learning
Interview Preparation
Resume Building

Always explain simply.

If code is requested,
give complete working code.
"""

history = []


def ask(question):

    history.append({
        "role": "user",
        "content": question
    })

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(history)

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        text,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True
    )

    response = tokenizer.decode(
        outputs[0][inputs.input_ids.shape[1]:],
        skip_special_tokens=True
    )

    history.append({
        "role": "assistant",
        "content": response
    })

    return response