from llmtuner import run_exp
from llmtuner.extras.misc import torch_gc


run_exp(dict(
  stage="sft",                        # 进行指令监督微调
  do_train=True,
  model_name_or_path="Qwen/Qwen1.5-7B-Chat", # 使用 Qwen1.5-7B-Chat 模型
  dataset="identity,COIG-CQIA-full",      # 使用 alpaca 和自我认知数据集
  template="qwen",                     # 使用 Qwen 模板
  finetuning_type="lora",                   # 使用 LoRA 适配器来节省显存
  lora_target="all",                     # 添加 LoRA 适配器至全部线性层
  output_dir="qwen_lora",                  # 保存 LoRA 适配器的路径
  per_device_train_batch_size=1,               # 批处理大小
  gradient_accumulation_steps=2,               # 梯度累积步数
  lr_scheduler_type="cosine",                 # 使用余弦学习率退火算法
  logging_steps=10,                      # 每 10 步输出一个记录
  warmup_ratio=0.1,                      # 使用预热学习率
  save_steps=1000,                      # 每 1000 步保存一个检查点
  learning_rate=3e-5,                     # 学习率大小
  num_train_epochs=1.0,                    # 训练轮数
  max_grad_norm=1.0,                     # 将梯度范数裁剪至 1.0
  lora_rank = 8,
  lora_alpha = 16,
  lora_dropout = 0,
  loraplus_lr_ratio=16.0,                   # 使用 LoRA+ 算法并设置 lambda=16.0
  use_unsloth=True,                      # 使用 UnslothAI 的 LoRA 优化来加快一倍的训练速度
  fp16=True,                         # 使用 float16 混合精度训练
))

torch_gc()