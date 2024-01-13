#! /usr/bin/env bash

set -ex

PRE_SEQ_LEN=128
LR=5e-3
NUM_GPUS=1
MAX_SEQ_LEN=2048
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=300
SAVE_INTERVAL=100

AUTORESUME_FROM_CHECKPOINT=True
DATESTR=`date +%Y%m%d-%H%M%S`
RUN_NAME=tool_alpaca_pt

BASE_MODEL_PATH=/mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b
DATASET_PATH=formatted_data/glm.jsonl
OUTPUT_DIR=output/test-202401132034-128-5e-3

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=1 finetune.py \
    --train_format multi-turn \
    --train_file formatted_data/glm.jsonl \
    --max_seq_length 2048 \
    --preprocessing_num_workers 1 \
    --model_name_or_path /mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b \
    --output_dir output/test-202401132034-128-5e-3 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --max_steps 300 \
    --logging_steps 1 \
    --save_steps 100 \
    --learning_rate 5e-3 \
    --pre_seq_len 128 \
    --resume_from_checkpoint True 2>&1 | tee output/test-202401132034-128-5e-3/train.log
