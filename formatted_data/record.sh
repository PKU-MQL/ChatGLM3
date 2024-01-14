#! /usr/bin/env bash

set -ex

PRE_SEQ_LEN=128
LR=1e-2
NUM_GPUS=1
MAX_SEQ_LEN=2048
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=500
SAVE_INTERVAL=100

AUTORESUME_FROM_CHECKPOINT=True
DATESTR=`date +%Y%m%d-%H%M%S`
RUN_NAME=test

BASE_MODEL_PATH=/mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b
DATASET_PATH=formatted_data/glm.jsonl
OUTPUT_DIR=output/${RUN_NAME}-${DATESTR}-${PRE_SEQ_LEN}-${LR}

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=$NUM_GPUS finetune.py \
    --train_format multi-turn \
    --train_file $DATASET_PATH \
    --max_seq_length $MAX_SEQ_LEN \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --per_device_train_batch_size $DEV_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUMULARION_STEPS \
    --max_steps $MAX_STEP \
    --logging_steps 1 \
    --save_steps $SAVE_INTERVAL \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN \
    --resume_from_checkpoint $AUTORESUME_FROM_CHECKPOINT 2>&1 | tee ${OUTPUT_DIR}/train.log


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


PRE_SEQ_LEN=128
LR=1e-2
NUM_GPUS=1
MAX_SEQ_LEN=2048
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=500
SAVE_INTERVAL=100

AUTORESUME_FROM_CHECKPOINT=True
DATESTR=`date +%Y%m%d-%H%M%S`
RUN_NAME=test

BASE_MODEL_PATH=/mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b
DATASET_PATH=formatted_data/glm2.jsonl
OUTPUT_DIR=output/test-202401132355-128-1e-2

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=1 finetune.py \
    --train_format multi-turn \
    --train_file formatted_data/glm2.jsonl \
    --max_seq_length 1024 \
    --preprocessing_num_workers 1 \
    --model_name_or_path /mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b \
    --output_dir output/test-202401132355-128-1e-2 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --max_steps 500 \
    --logging_steps 1 \
    --save_steps 100 \
    --learning_rate 1e-2 \
    --pre_seq_len 128 \
    --resume_from_checkpoint True 2>&1 | tee output/test-202401132355-128-1e-2/train.log
