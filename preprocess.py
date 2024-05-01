import json


NAME = "模型名字"
AUTHOR = "作者名字"

with open("dataset/identity.json", "r", encoding="utf-8") as f:
  dataset = json.load(f)

for sample in dataset:
  sample["output"] = sample["output"].replace("NAME", NAME).replace("AUTHOR", AUTHOR)

with open("data/identity.json", "w", encoding="utf-8") as f:
  json.dump(dataset, f, indent=2, ensure_ascii=False)