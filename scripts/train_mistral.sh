#!/usr/bin/env bash
# LoRA fine-tuning of mistralai/Mistral-7B-Instruct-v0.2 on Essay-Syntax-Instruct, as for the released adapter.
set -euo pipefail
cd "$(dirname "$0")/../training"

accelerate launch --config_file ../configs/accelerate_deepspeed.yaml train.py \
  --seed 100 \
  --model_name_or_path "mistralai/Mistral-7B-Instruct-v0.2" \
  --dataset_name "Kamyar-zeinalipour/AFG_Mistral_v2" \
  --chat_template_format "none" \
  --add_special_tokens False \
  --append_concat_token False \
  --splits "train,test" \
  --max_seq_len 2048 \
  --num_train_epochs 3 \
  --logging_steps 5 \
  --evaluation_strategy "epoch" \
  --save_strategy "epoch" \
  --bf16 True \
  --packing False \
  --learning_rate 1e-4 \
  --lr_scheduler_type "cosine" \
  --weight_decay 1e-4 \
  --warmup_ratio 0.0 \
  --max_grad_norm 1.0 \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --gradient_checkpointing True \
  --use_reentrant False \
  --use_flash_attn True \
  --use_peft_lora True \
  --lora_r 32 \
  --lora_alpha 64 \
  --lora_dropout 0.1 \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj,down_proj,up_proj,gate_proj,embed_tokens,lm_head" \
  --output_dir "../outputs/mistral" \
  --report_to none
