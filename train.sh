CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train True \
    --model_name_or_path Qwen/Qwen1.5-7B-Chat \
    --finetuning_type full \
    --template qwen \
    --flash_attn auto \
    --dataset_dir data \
    --dataset COIG-CQIA-full,GLM-4-Instruct-4K-zh,Claude3-Opus-Multi-Instruct-5K,identity \
    --cutoff_len 1024 \
    --learning_rate 2e-05 \
    --num_train_epochs 1.0 \
    --max_samples 100000 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 5 \
    --save_steps 100 \
    --warmup_steps 0 \
    --optim adamw_torch \
    --report_to none \
    --output_dir saves/LLaMA3-8B-Chat/full/train_2024-05-06-02-10-40 \
    --fp16 True \
    --plot_loss True