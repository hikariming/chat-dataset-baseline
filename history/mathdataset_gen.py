import random
import json

def generate_dataset(num_questions):
    dataset = []
    operations = ['+', '-', '*', '/']

    for _ in range(num_questions):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(operations)

        if operation == '+':
            instruction = f"{num1}+{num2}="
            answer = num1 + num2
        elif operation == '-':
            instruction = f"{num1}-{num2}="
            answer = num1 - num2
        elif operation == '*':
            instruction = f"{num1}*{num2}="
            answer = num1 * num2
        else: # operation == '/'
            instruction = f"{num1}/{num2}="
            answer = round(num1 / num2, 2)

        dataset.append({
            "instruction": instruction,
            "input": "",
            "output": f"{instruction}{answer}"
        })

    return dataset

math_dataset = generate_dataset(500)

# 将数据集保存到名为“整数加减法.json”的文件中
with open("./整数加减法.json", "w", encoding="utf-8") as file:
    json.dump(math_dataset, file, ensure_ascii=False, indent=4)
